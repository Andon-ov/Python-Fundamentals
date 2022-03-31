#
# # създаваме клас
# class Email:
#     # метода получава атрибути (метод се нарича функция в класа)
#     def __init__(self,sender, receiver, content):
#         # това са параметри
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#         self.is_send = False
#     # метод сенд който изпраща писмата
#     def send(self):
#         self.is_send = True
#     # метод гет който ни дава информация за принта
#     def get_info(self):
#         return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"
#
#
# command_input = input()
# # създаваме лист с имейли
# emails = []
# while not command_input == "Stop":
# # сплитваме командата на сендър , ресивър и контент
#     s,r,c = command_input.split()
#     # command_args = command_input.split()
#     # s = command_input[0]
#     # r = command_input[1]
#     # c = command_input[2]
#
# # добавяме го към класа и към листа
#     email = Email(s,r,c)
#     emails.append(email)
#     command_input = input()
# # взимаме стринг на кой индекси ще изпратим имейлите - и го обръщаме в инт
# indexes = [int(i) for i in input().split(", ")]
# # въртим през лисата за да намерим кой индекси отговарят на желаните
# for index in indexes:
#     # прекарваме ги през метода сенд - става True
#     emails[index].send()
# # въртим цикал за да принтираме целия списък с метода гет
# for email in emails:
#     print(email.get_info())


class Email():
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
line = input()
while not line == "Stop":
    sender, receiver, content = line.split()
    email = Email(sender, receiver, content)
    emails.append(email)

    line = input()

send_email = [int(x) for x in input().split(", ")]

for index in send_email:
    emails[index].send()

for email in emails:
    print(email.get_info())
