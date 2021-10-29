#LINEAR SEARCH
l = int(input("enter nos in list: "))
p=[]
for i in range(l):
  p.append(int(input("")))

n=int(input("enter no to search: "))

for i in range(len(p)):
  if p[i]==n:
    print("Number found")
    break
else:
  print("Number not found")
  
#SENTINEL SEARCH
l = int(input("enter nos in list: "))
p=[]
for i in range(l):
  p.append(int(input("")))

key=int(input("enter no to search: "))

def sentinel_Search(p, n, key):
    last = p[n - 1]
    p[n-1] = key
    i=0
 
    while (p[i] != key):
        i+=1
    p[n-1]=last
 
    if ((i<n-1) or (p[n-1] == key)):
        print("Number found")
    else:
        print("Number not found")

sentinel_Search(p, n, key)
