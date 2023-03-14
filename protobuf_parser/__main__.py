import pr_pb2 as pb


msg = pb.WrapperMessage()
msg.request_for_slow_response.time_in_seconds_to_sleep = 12
print(msg)
