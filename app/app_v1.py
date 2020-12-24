print("Enter the pyramid length: ",end='')
l=int(input())
for i in range(l):
    for j in range(i):
        print("*",end='\t')
    print()
