number_list = input().split()
while True:
    comm = input()
    if comm == "Finish":
        print(*number_list)
        break
    command = comm.split()

    if command[0] == 'Add':
        number_list.append(command[1])
    if command[0] == "Remove":
        if command[1] in number_list:
            number_list.remove(command[1])
    if command[0] == "Replace":
        if command[1] in number_list:
            item_index = number_list.index(command[1])
            number_list[item_index] = command[2]
    if command[0] == "Collapse":
        number_list = [int(j) for j in number_list]
        check_number = int(command[1])
        number_list = [s for s in number_list if s >= check_number]