def add_to_exam(dict, name, point):
    if name not in dict:
        dict[name] = []
    dict[name].append(point)


def add_submissions(dict, lang, point):
    if lang not in dict:
        dict[lang] = 0
    dict[lang] += 1
    return dict


def ban(dict, name):
    del dict[name]
    return dict


exam = {}
submissions = {}

command = input()
while not command == "exam finished":
    command_split = command.split("-")
    username = command_split[0]
    language = command_split[1]
    if not language == "banned":
        points = int(command_split[2])
        add_to_exam(exam, username, points)
        add_submissions(submissions, language, points)
    else:
        ban(exam, username)

    command = input()
print(f"Results:")
for key, value in exam.items():
    print(f"{key} | {max(value)}")
print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")
