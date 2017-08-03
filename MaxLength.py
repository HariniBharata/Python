n=int(input("how many words?"))
i=0
m=n
w=[]
l=[]
for i in range(0,n):
    word=input("enter the word")
    w.append(word)
    k=len(w[i])
    l.append(k)
max=0
for i in range(0,m):
    if l[i]>max:
        max=l[i]
print("the maximum len is:",max)

