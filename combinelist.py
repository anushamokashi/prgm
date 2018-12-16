import itertools

key=[1,2,3,4,5]
value=['a','b','c','d','e']
dictionary=dict(zip(key,value))
print dictionary



# if i give more keys or values use itertools(bt code didnt work check it)
key=[1,2,3,4,5]
value=['a','b','c','d','e','f']
dictionary=dict(itertools.izip(key,value))
print dictionary



