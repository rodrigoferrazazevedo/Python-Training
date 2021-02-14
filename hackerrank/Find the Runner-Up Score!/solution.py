if __name__ == '__main__':

    n = int("5")
    arr = map(int, "2 3 6 6 5".split())
    
    if(2<=n<=10):
        lst = (list(arr)).sort(reverse=True)

        print(lst)

        print(list(arr))
