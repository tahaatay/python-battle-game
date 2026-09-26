import time
start=time.time()
print(0.1+0.2)
for i in range(1,100001):
    print(i)

stop=time.time()
print(f"\n{stop-start}")


