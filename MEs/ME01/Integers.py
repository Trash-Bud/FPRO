num = float(input())
ints = [1, 2, 2, 3, 5, 9, 13, 21, 34]
g = []
l = []
for i in range(0, len(ints)):
    n = ints[i]
    if n == num:
        pass
    elif n < num:
        l.append(n)
    else:
        g.append(n)

if len(l) != 0:
    print("Less:", end = " ")
else:
   print("Less:") 

for e in range(0, len(l)):
    if e == len(l) - 1:
        print(l[e])
    else:
        print(l[e], end = " ")

print ("Greater:", end = " ")
for e in range(0, len(g)):
    print(g[e], end = " ")
       


    