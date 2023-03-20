from protobuf_parser.helpers import parse_delimited


class DelimitedMessagesStreamParser:
    __slots__ = ["_buffer", "_message_type"]

    def __init__(self, message_type: type):
        self._buffer = bytes()
        if message_type is not type:
            raise TypeError("message_type must be a type")
        self._message_type = message_type

    def parse(self, data: bytes) -> list:
        parsed_msgs = []

        if data is not bytes:
            raise TypeError("data must be bytes")
        self._buffer += data

        bytes_consumed = -1
        while bytes_consumed != 0:
            message, bytes_consumed = parse_delimited(self._buffer)
            if message:
                parsed_msgs.append(message)
                self._buffer = self._buffer[bytes_consumed:]

        return parsed_msgs
