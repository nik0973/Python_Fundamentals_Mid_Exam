numeric = [int(n) for n in input().split()]
while True:
    command = input()
    if command == 'end':
        break
    if command == "decrease":
        numeric = [num - 1 for num in numeric]
        continue
    command = command.split()
    index1, index2 = int(command[1]), int(command[2])
    if command[0] == 'swap':
        numeric[index1], numeric[index2] = numeric[index2], numeric[index1]
    elif command[0] == 'multiply':
        first = numeric[index1]
        second = numeric[index2]
        sum = first * second
        numeric[index1] = sum
        # numeric.insert(index1, sum)
    # elif command[0] == 'decrease':
    #     numeric = [num - 1 for num in numeric]
print(*numeric, sep=', ')