#decorators are used to boost up functions. i.e. use to enhance functions.
#Higher order functions are funcitons who take other function as argument.
#Let's make our own decorators

def my_decorator(arg_func):
    def wrap_function():
        print('***********')
        arg_func()
        print('***********')
    return wrap_function()

@my_decorator
def print_hello():
    print('Hellooooo')


#print_hello

@my_decorator
def print_bye():
    print('Buh-Byeee')



#my_decorator(print_hello)()
