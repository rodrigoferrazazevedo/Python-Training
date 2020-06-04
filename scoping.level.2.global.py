def outer():
    test = 1
    def inner():
        global test
        test = 2
        print('inner: ', test, ' with id ', id(test))

    inner()
    print('outer: ', test, 'with id ', id(test))

test = 0
outer()
print('global: ', test, 'with id ', id(test))
