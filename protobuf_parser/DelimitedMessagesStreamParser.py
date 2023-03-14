from helpers import parse_delimited
import pr_pb2 as pb


class DelimitedMessagesStreamParser:
    __slots__ = "_buffer"

    def __init__(self):
        self._buffer = bytes()

    def parse(self, data: bytes) -> list[pb.WrapperMessage]:
        parsed_msgs = []
        self._buffer += data

        bytes_consumed = -1
        while bytes_consumed != 0:
            message, bytes_consumed = parse_delimited(self._buffer)
            if message is not None:
                parsed_msgs.append(message)
                self._buffer = self._buffer.removeprefix(self._buffer[:bytes_consumed])

        return parsed_msgs
