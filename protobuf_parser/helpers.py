from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.message import DecodeError

import pr_pb2 as pb


def serialize_delimited(message: pb.WrapperMessage) -> bytes:
    """Serialize message to bytes"""
    message_size = message.ByteSize()
    res = _VarintBytes(message_size) + message.SerializeToString()
    return res


def parse_delimited(data: bytes) -> (pb.WrapperMessage, int):
    """Parsing byte data to message, returning message and consumed bytes"""
    try:
        msg_size, pos = _DecodeVarint32(data, 0)
        msg = pb.WrapperMessage()
        msg.ParseFromString(data[pos:(pos + msg_size)])
    except (DecodeError, IndexError):
        return None, 0

    return msg, pos + msg_size
