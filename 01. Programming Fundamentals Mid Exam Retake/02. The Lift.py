number_of_people = int(input())
free_spots = [int(s) for s in input().split()]
max_people_tobring = 4

for i in range(len(free_spots)):
    max_bring = min(max_people_tobring - free_spots[i], number_of_people)
    free_spots[i] += max_bring
    number_of_people -= max_bring

if number_of_people > 0:
    print(f"There isn't enough space! {number_of_people} people in a queue!")
if min(free_spots) < 4:
    print("The lift has empty spots!")
print(" ".join(str(j) for j in free_spots))

