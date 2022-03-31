def data_types(command, type):
    if command == 'int':
        data = int(type) * 2

    elif command == 'real':
        data = f'{(float(type) * 1.5):.2f}'

    elif command == 'string':
        data = f'${type}$'

    return data


real_command = input()
real_type = input()

print(data_types(real_command, real_type))
