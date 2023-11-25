book_list = input().split('&')
while True:
    comm = input()
    if comm == "Done":
        break
    command = comm.split(" | ")

    if command[0] == 'Add Book':
        if command[1] not in book_list:
            book_list.insert(0, command[1])
    if command[0] == "Take Book":
        if command[1] in book_list:
            book_list.remove(command[1])
    if command[0] == "Swap Books":
        if command[1] in book_list and command[2] in book_list:
            index1 = book_list.index(command[1])
            index2 = book_list.index(command[2])
            book_list[index1], book_list[index2] = book_list[index2], book_list[index1]
    if command[0] == "Insert Book":
        if command[1] not in book_list:
            book_list.append(command[1])
    if command[0] == "Check Book":
        check_index = int(command[1])
        if check_index <= len(book_list) -1 and check_index >= 0:
            print(book_list[check_index])
print(*book_list, sep=', ')
