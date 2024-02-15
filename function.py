def main():
    x=int(input())
    M=int(input())
    for n in range(1,M):
        if(x*n)%M==1:
            return n
        else:
            return"int not exist"
print(ain())