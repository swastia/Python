#create a list using list comprehensions

list1 = [char for char in 'helloooo']
list2 = [num for num in range(0,100) if num%2==0]
print(list1)
print(list2)

#create a set using comprehensions
set1 = {char for char in 'helloooo'}
set2 = {num**2 for num in range(0,100) if num%2==0}
print(set1)
print(set2)

#create a dictionary using comprehensions

my_dict = {
    'a' : 1,
    'b' : 2
}

new_dict = {k:v*2 for k,v in my_dict.items()}
new_dict2 = {k:v*2 for k,v in my_dict.items() if v%2==0}

print(new_dict)

print(new_dict2)


#more on dictionary. Creating dicitonaries using list k= item, v= item*2
new_dict3 = {num:num*2 for num in [1,2,3]}
print(new_dict3)