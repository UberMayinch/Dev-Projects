
import numpy as np
import time

a = list(np.random.randint([100]*10000))
b = list(np.random.randint([100]*10000))


# O(n^2)
start_nai = time.time()
print(a)
common = []
for e in a:
    for f in b:
        if e == f and e not in common:
            common.append(e)

end_nai = time.time()
common = sorted(common)

# O(nlogn)

start_opt = time.time()
common2 = []
a = np.unique(a)
b = np.unique(b)
print(a)
for f in b:
    if f in a and f not in common2:
        common2.append(f)

# common2 = set(common2)
end_opt = time.time()

print(end_nai - start_nai)
print(end_opt - start_opt)
print(common)
print(common2)
