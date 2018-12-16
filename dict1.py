'''dict1={'k1':'v1' , 'k2':'v2'}
dict2={'k3':'v3', 'k4':'v4'}
dict3={'k5':'v5', 'k6':'v6'}

d1 = {}
for d in [dict1,dict2,dict3]:
    d1.update(d)
    print d'''



from itertools import chain
x={'k1':'v1' , 'k2':'v2'}
y={'k3':'v3', 'k4':'v4'}
w={'k2':'v2', 'k6':'v6'}
z =dict(set(chain(x.iteritems(), y.iteritems() ,w.iteritems())))
print z
