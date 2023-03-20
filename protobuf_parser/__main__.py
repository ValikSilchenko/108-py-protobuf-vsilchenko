import pr_pb2 as pb
from DelimitedMessagesStreamParser import DelimitedMessagesStreamParser
from helpers import serialize_delimited

msg = pb.WrapperMessage()
msg.request_for_slow_response.time_in_seconds_to_sleep = 229

parser = DelimitedMessagesStreamParser(pb.WrapperMessage)
data = bytes()
for i in range(5):
    msg.request_for_slow_response.time_in_seconds_to_sleep = 2 * i
    data += serialize_delimited(msg)
res = parser.parse(data)
print(*res, sep='\n')
