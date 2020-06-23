alphabet = ['a','b','d','e','i','j','o']
vowels = ['a','e','i','o','u']

# def filterVolwels(alphabet):  
#     if(alphabet in vowels):
#         return True
#     else:
#         return False

#filteredVolwels = filter(filterVolwels, alphabet)

filteredVolwels = filter(lambda x: x in vowels, alphabet)

#print(list(filteredVolwels))

print('The filtered volwels are:')
for volwel in filteredVolwels:
    print(volwel)