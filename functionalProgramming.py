#Maps
from functools import reduce
num_list = [1,2,3]
to_zip1 = [400,500,600]
to_zip2 = [100,200,300]

def multiply_by_2(item):
    return item*2

def only_odds(item):
    if item % 2!= 0:
        return item

def accumulator(acc,item):
    print(acc,item)
    return acc+item

#map
print(list(map(multiply_by_2, num_list)))
#filter
print(list(filter(only_odds, num_list)))
#zip
print(list(zip(to_zip1,to_zip2, num_list)))
#reduce
print(reduce(accumulator, num_list, 100))

print(num_list)