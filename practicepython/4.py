import time

num = int(input())
div = []
i = 1

start_opt = time.time()
while i * i <= num:
    if num % i == 0:
        div.append(i)
        div.append(num / i)
    i+=1
end_opt = time.time()

start_naive = time.time()
for i in range(1, num+1):
    if num % i == 0:
        div.append(i)
end_naive = time.time()

print(end_naive - start_naive)
print(end_opt-start_opt)
print(div)