num = int(input("Enter num"))
lst = list(item for item in list(map(int, input().split())) if item < num)
print(lst)

