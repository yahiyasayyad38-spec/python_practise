# data type (str,list,dict,tuple,set)
# list comprehension
# func
# lambda, filter, map, reduce

def string_operation():
    string = ' python words '
    print(string.capitalize())
    print(string.upper())
    print(string.lower())
    print(string.index('r'))
    print(string.strip())
    print(string.lstrip())
    print(string.rstrip())
    print(string.split())
    print(string.join(['series']))
    print(string.isalpha()) # only alphabates
    print(string.isalnum()) # only alphabates + numbers
    print(string.isdigit()) # only numbers
    print(string.count('')) # only numbers
    print(string.replace(' ','_'))
    print(string)
    # print(dir(str))
# string_operation()


import pandas as pd


people = {
    'first_name' : ['bleas','charlie','alies'],
    'last_name': ['doe','kate','john'],
    'email' : ['belas@gmail.com','charlie@gmail.com','alies@gmail.com']
}

df = pd.DataFrame(people)
print(df)
print(df.head())
print(df.shape)




