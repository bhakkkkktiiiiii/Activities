'''(a) In few chit-chat programs, there is a limitation on the number of letters that you can send to your family and friends.

Write a function that takes as input the,

message and checks whether the number of letters is less than 200 or above. If the length of the information is less than 200, the chat should be returned.


If the length of the chat is greater than 200, data consisting of only the first 200 characters should be returned.
'''
def limit_message(message):
    if len(message) <= 200:
        return message
    else:
        return message[0:200]
message=input()
print(limit_message(message))
  


