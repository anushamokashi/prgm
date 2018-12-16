'''powerset=([1,2,3])
from itertools import chain,combinations
def powerset(iterable):
	xs= list(iterable)
	return chain.from_iterable(combinations(xs,n) for n in range (len(xs)+1))
powerset()'''


'''from itertools import combinations, chain
n=raw_input("enter num")
allsubsets = lambda n: list(chain(*[combinations(range(n), ni) for ni in range(n+1)]))

print allsubsets(3)'''

'''def subsets(my_set):
    result = [[]]
    for x in my_set:
        result = result + [y + [x] for y in result]
    return result
    print result'''

'''def subsets(mySet):
    return reduce(lambda z, x: z + [y + [x] for y in z], mySet, [[]])'''

from itertools import chain, combinations

def all_subsets(ss):

    return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))
    print'ss'

for subset in all_subsets([1, 2, 3, 4]):
      print(subset)