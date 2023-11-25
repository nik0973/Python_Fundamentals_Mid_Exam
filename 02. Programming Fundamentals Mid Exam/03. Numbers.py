numeric = [int(s) for s in input().split()]
aver = sum(numeric) / len(numeric)
greater = [f for f in numeric if f > aver]
sort_list = sorted(greater, reverse=True)
cut = sort_list[0:5]
if not cut:
    print('No')
if len(cut) < 5:
    print()
# print(aver)
# print(*sort_list)
print(*cut)
