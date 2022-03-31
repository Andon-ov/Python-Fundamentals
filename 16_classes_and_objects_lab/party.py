# Create a class Party that only has an attribute people – empty list. The __init__ method should not accept any parameters.
# You will be given names of people (on separate lines) until you receive the command "End".
# Use the created class to solve this problem. After you receive the "End" command, print 2 lines:
# •	"Going: {people}" - the people should be separated by comma and space ", "
# •	"Total: {total_people_going}"

# # Създаваме клас
# class Party:
#     def __init__(self):
#         self.people = []
#     # създаваме гет - за да достъпим инфото от класа
#     def get_info(self):
#         # създаваме променлива която даостъпва листа
#         people_res = ', '.join(self.people)
#         # може вместо \n да използваме """  """ и между тях да напишем кода който да се пренесе на нов ред
#         return f"Going: {people_res}\nTotal: {len(self.people)}"
# # взимаме инпут
# person_input = input()
# # извикваме класът
# party = Party()
# while not person_input == "End":
#     # добавяме хората към лист в класът
#     party.people.append(person_input)
#
#     person_input = input()
# # създаваме променлива която достъпва ретърна
# info = party.get_info()
# print(info)


class Party:
    def __init__(self):
        self.people = []


person_input = input()

party = Party()
while not person_input == "End":

    party.people.append(person_input)

    person_input = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")