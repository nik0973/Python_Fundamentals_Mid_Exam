food = float(input())
hay = float(input())
cover = float(input())
guinea_weight = float(input())
count = 0
for i in range(1, 30+1):
        food -= 0.300
        if i % 2 == 0:
            hay -= food * 0.05
        if i % 3 == 0:
            cover -= guinea_weight * 1/3
        if food <= 0 or hay <= 0 or cover <= 0:
            print("Merry must go to the pet store!")
            break
else:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")


