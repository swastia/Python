#square

my_list = [5,4,3]

squared_list = list(map(lambda num : num**2, my_list))
print(squared_list)

#sortList

a = [(10,-1), (5,2), (8,5), (0,1)]

#sorting based on first value
a.sort()
print(a)

#sorting based on second value in the list
a.sort(key= lambda item : item[1])
print(a)

