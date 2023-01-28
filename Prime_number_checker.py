num = int(input())
for i in range(2,num):
    if num == 2:
        print("Prime")
        exit()
    elif num % i == 0:
        print("Not Prime")
        exit()
else:
    print("Prime")