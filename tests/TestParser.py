from unittest import TestCase
from protobuf_parser import *


class TestParser(TestCase):
    n = 5
    num = 2

    def test_full_message_sending(self):
        parser = DelimitedMessagesStreamParser(pb.WrapperMessage)
        msg = pb.WrapperMessage()
        data = bytes()
        for i in range(self.n):
            msg.request_for_slow_response.time_in_seconds_to_sleep = self.num * i
            data += serialize_delimited(msg)
        res = parser.parse(data)

        self.assertEqual(len(res), self.n)
        for i in range(self.n):
            self.assertTrue(res[i].HasField("request_for_slow_response"))
            self.assertEqual(res[i].request_for_slow_response.time_in_seconds_to_sleep, self.num * i)

    def test_partial_message_sending(self):
        parser = DelimitedMessagesStreamParser(pb.WrapperMessage)
        msg = pb.WrapperMessage()
        data = bytes()
        for i in range(self.n):
            msg.request_for_slow_response.time_in_seconds_to_sleep = self.num * i
            data += serialize_delimited(msg)

        res = parser.parse(data[:(len(data) // 2)])

        self.assertEqual(len(res), self.n // 2)

        res += parser.parse(data[(len(data) // 2):])
        self.assertEqual(len(res), self.n)
        for i in range(self.n):
            self.assertTrue(res[i].HasField("request_for_slow_response"))
            self.assertEqual(res[i].request_for_slow_response.time_in_seconds_to_sleep, self.num * i)

    def test_wrong_message_format(self):
        parser = DelimitedMessagesStreamParser(pb.WrapperMessage)
        data = "123456678".encode("utf-8")
        self.assertEqual(parser.parse(data), [])
        data = bytes()
        self.assertEqual(parser.parse(data), [])
