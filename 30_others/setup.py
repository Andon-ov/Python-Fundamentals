
import sys
from io import StringIO

input1 = """Peter John Hi,John
John Peter Hi,Peter!
Katy Lilly Hello,Lilly
Stop
0, 2"""

sys.stdin = StringIO(input1)


class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
command = input()
while not command == "Stop":
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    emails.append(email)

    command = input()

index = [int(x) for x in input().split(", ")]
for index in index:
    emails[index].send()

for email in emails:
    print(email.get_info())
