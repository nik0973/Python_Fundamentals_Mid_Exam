employ1 = int(input())
employ2 = int(input())
employ3 = int(input())
number_of_students = int(input())
efficiency_for_hour = employ1 + employ2 + employ3
answered = 0
hour = 0
count = 0
while answered < number_of_students:
    count += 1
    if count == 4:
        count = 0
        if answered >= number_of_students:
            break
        else:
            hour += 1
            continue
    answered += efficiency_for_hour
    hour += 1
    # number_of_students -= efficiency_for_hour

        # number_of_students = number_of_students
print(f"Time needed: {hour}h.")




# print(efficiency_for_hour)

