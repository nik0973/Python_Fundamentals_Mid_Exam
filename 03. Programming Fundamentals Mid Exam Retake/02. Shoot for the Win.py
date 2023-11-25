shot_list = [int(s) for s in input().split()]
count = 0
index_list = []
while True:
    command = input()
    if command == 'End':
        print(f"Shot targets: {count} -> {' '.join(str(f) for f in shot_list)}")
        break

    if int(command) <= len(shot_list)-1:
        current_number = shot_list[int(command)]
        if shot_list[int(command)] != -1:
            count += 1
            shot_list[int(command)] = -1
            for i in range(len(shot_list)):
                if shot_list[i] == -1:
                    continue
                else:
                    if shot_list[i] > current_number:
                        shot_list[i] -= current_number
                    elif shot_list[i] <= current_number:
                        shot_list[i] += current_number
    else:
        continue



