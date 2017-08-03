print("Enter a string")
s = input()
l = 0 
u = len(s)-1
f = 1
while l < u:
    if(s[l] != s[u]):
        print(s+" is not a palindrome")
        f = 0
        break
    l = l+1
    u = u-1
if f==1:
    print(s+" is a palindrome")
        
    
    
