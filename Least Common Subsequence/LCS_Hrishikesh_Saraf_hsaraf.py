import numpy as np
print "Computing LCS.."
file=open('input.txt','r')
String=[]
for i in file:
    String.append(i)

String1=String[0]
String2=String[1]
String1=String1.rstrip()
String2=String2.rstrip()

A=[]
for i in String1:
    A.append(i)

B=[]
for i in String2:
    B.append(i)


n=len(String1)
m=len(String2)
opt=np.zeros((n+1,m+1))
res=np.zeros((n,m))

for i in range(0,n):
    for j in range(0,m):
        opt[i][0]=0
        if A[i]==B[j]:
            opt[i][j]=opt[i-1][j-1]+1
            res[i][j]=1
        elif opt[i][j-1]>=opt[i-1,j]:
            opt[i][j]=opt[i][j-1]
            res[i][j] = 2
        else:
            opt[i][j]=opt[i-1][j]
            res[i][j] = 3

LCSval=np.amax(opt)
LCSval=int(LCSval)

i=n-1
j=m-1
S=[]
while i>=0 and j>=0:
    if res[i][j]==1:
        S.append(A[i])
        i=i-1
        j=j-1
    elif res[i][j]==3:
        i=i-1
    else:
        j=j-1

n=len(S)-1
T=[]
FString=''
while(n>=0):
    FString=FString+S[n]
    T.append(S[n])
    n=n-1

print LCSval
print FString

file=open("output.txt",'w')
file.write(str(LCSval))
file.write("\n")
file.write(FString)
file.close()




