def my_function():
    test = 1
    print('my_function: ', test, ' with id ', id(test))

test = 0
my_function()
print('global: ', test, ' with id ', id(test))
