for _ in range(int(input())):
    n = int(input())
    flag=0
    for i in range (1,n+1):
        if (i*i)==n :
            print("1")
            flag =1
            break


    if  flag == 0 :
        print("0")



if __name__ == '__main__':
    pass

