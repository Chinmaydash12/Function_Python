#function
'''def add():
    print('Hello')'''
'''a=5
def add():
    print(a)'''
'''a=5
def add():
    print(a)
def sub():
    a=20
    print(a)
    b=30
    print(b)'''
'''a=5
def add():
    a=10
    print(a)
    def sub():
        print(a)
        b=30
        print(b)
    print(a)
    sub()
add()# to call function 
print(a)'''

a=10
def add():
    print(a)
    def sub():
        b=20
        a=30
        print(a)
        print(b)
    sub()
    print(a)
    print(b)
add()
print(a)


