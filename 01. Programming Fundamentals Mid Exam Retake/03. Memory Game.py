def main():
    strings = input().split()
    count = 0
    while True:
        command = input()
        count += 1
        if command == "end":
            print(f"Sorry you lose :(\n {' '.join(strings)}")
            break
        index1, index2 = map(int, command.split())

        if is_invalid(index1, index2, strings):
            handle_invalid(strings, count)
        else:
            handle_valid(index1, index2, strings, count)

def is_invalid(index1, index2, strings):
    return (index1 == index2 or
            index1 < 0 or
            index2 < 0 or
            index1 >= len(strings) or
            index2 >= len(strings)
            )

def handle_invalid(strings, count):
    middle_point = len(strings) // 2
    strings.insert(middle_point, f'-{count}a')
    strings.insert(middle_point, f'-{count}a')
    print(f"Invalid input! Adding additional elements to the board")

def handle_valid(index1, index2, strings, count):
    if strings[index1] == strings[index2]:
        print(f"Congrats! You have found matching elements - {strings[index1]}!")
        second_element = strings[index2]
        strings.pop(index1)
        strings.remove(second_element)
    else:
        print(f"Try again!")
    if len(strings) == 0:
        print(f"You have won in {count} turns!")
        exit()

main()