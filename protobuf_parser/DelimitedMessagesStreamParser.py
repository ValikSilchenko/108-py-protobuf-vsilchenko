from protobuf_parser.helpers import parse_delimited


class DelimitedMessagesStreamParser:
    __slots__ = ["_buffer", "_message_type"]

    def __init__(self, message_type: type):
        self._buffer = bytes()
        self._message_type = message_type

    def parse(self, data: bytes) -> list:
        parsed_msgs = []

        if type(data) is not bytes:
            return []
        self._buffer += data

        bytes_consumed = -1
        while bytes_consumed != 0:
            message, bytes_consumed = parse_delimited(self._buffer, self._message_type)
            if message:
                parsed_msgs.append(message)
                self._buffer = self._buffer[bytes_consumed:]

        return parsed_msgs
