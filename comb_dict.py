l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e']
d1 = {}
for l1_ in l1:
    for l2_ in l2:
        d1[l1_] = l2_
        l2.remove(l2_)
        break  

print (d1)
