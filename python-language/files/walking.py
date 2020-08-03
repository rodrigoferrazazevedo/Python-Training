import os

for root, dirs, files in os.walk('.'):
    print(os.path.abspath(root))
    if dirs:
        print('Directories:')
        for dir_ in dirs:
            print(dir_)

    if files:
        print('Files:')
        for filename in files:
            print(filename)
        print()