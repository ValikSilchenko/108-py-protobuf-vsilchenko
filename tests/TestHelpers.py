from unittest import TestCase
from google.protobuf.internal.encoder import _VarintSize
from protobuf_parser import *


class TestHelpers(TestCase):
    num = 2

    def test_full_message_sending(self):
        message = pb.WrapperMessage()
        message.request_for_fast_response.SetInParent()
        result_msg, bytes_consumed = parse_delimited(serialize_delimited(message))
        self.assertTrue(result_msg.HasField("request_for_fast_response"))
        self.assertEqual(bytes_consumed, _VarintSize(message.ByteSize()) + message.ByteSize())

    def test_partial_message_sending(self):
        message = pb.WrapperMessage()
        message.request_for_fast_response.SetInParent()
        data = serialize_delimited(message)
        result_msg, bytes_consumed = parse_delimited(data[:(len(data) // 2)])
        self.assertIsNone(result_msg)
        self.assertEqual(bytes_consumed, 0)

        result_msg, bytes_consumed = parse_delimited(data)

        self.assertTrue(result_msg.HasField("request_for_fast_response"))
        self.assertEqual(bytes_consumed, _VarintSize(message.ByteSize()) + message.ByteSize())
