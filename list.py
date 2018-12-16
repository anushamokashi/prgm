'''list1=[0,1,2,3,4,5,6,7,8,9]
for i in list1:
    i=i+1
    print i'''

'''list=[]
for i in range(0,10):
    list.append(i)
    print list'''

list1=[]
list={'k1':'v1' , 'k2':'v2', 'k3':'v3'}
for i in list.items():
	
   # print i[0] , i[1]
    list1.append(list)
print list1

'''list1=[]
list={'k1':'v1' , 'k2':'v2', 'k3':'v3'}
for i in list.items():
    #print i[0] , i[1]
    list1=list.copy()
    list1.update(list)
print list1'''
