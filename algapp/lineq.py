import numpy as np
from scipy import linalg as la
#print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("*** The following application will solve 3-variable linear equations ***\n")
var=3
teq=[[],[],[]]
for i in range(var):
    print("\nEnter the co-efficients for Equation "+str(i+1))
    #for j in range(i+1):
    teq[i].append(int(input("Enter cf of X:")))
    teq[i].append(int(input("Enter cf of Y:")))
    teq[i].append(int(input("Enter cf of Z:")))
print(teq)
val=[int(input("Enter solution for equation 1: ")),int(input("Enter solution for equation 2: ")),int(input("Enter solution for equation 3: "))]
print(val)
'''eq1=[1,-1,1]
eq2=[-5,8,-9]
eq3=[1,-1,1]
val=[67,98,32]'''
print("\nYour Equations are as follows...\n")


for i in range(var):
    eq=str(teq[i][0])+"x"
    if teq[i][1]>0:
        eq=eq+"+"+str(teq[i][1])+"y"
    else:
        eq=eq+str(teq[i][1])+"y"
    if teq[i][2]>0:
        eq=eq+"+"+str(teq[i][2])+"z = "+str(val[i])
    else:
        eq=eq+str(teq[i][2])+"z = "+str(val[i])
    print(eq)

try:
    arr=np.array([teq[0],teq[1],teq[2]])
    print("\nThe solutions for x,y,z are as follows: ")
    print("x = "+str(round(la.solve(arr,val)[0],2)))
    print("y = "+str(round(la.solve(arr,val)[1],2)))
    print("z = "+str(round(la.solve(arr,val)[2],2)))
    eq=input("Press 'enter' key to exit: ")
except np.linalg.LinAlgError as err:
    print(err)
    if 'singular' in str(err):
        print("The equation you provided results in a singular matrix having a zero determinant value. This equation in not solvable.")
        eq=input("Press 'enter' key to exit: ")
