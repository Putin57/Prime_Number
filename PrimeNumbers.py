def is_prime(n):
    if n==0 or n==1:
        return False
    divisor=0
    for i in range(1,n+1):
        if n%i==0:
            divisor+=1
    if divisor==2:return True
    else:return False
    

for i in range(1,int(input())+1):
    if is_prime(i):
        print(i,end=" ")
print()
