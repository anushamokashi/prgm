
listA = [1, 2, 3, 4, 5]
    listB = ["red", "blue", "orange", "black", "grey"]

    b_iter = iter(listB)
 
    for item in listA:
       print item, next(b_iter)

