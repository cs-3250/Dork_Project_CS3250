def sum(a,b):
    return a +b
total = sum(8,4)
print('Eight Plus Four Is:', total)

def sum(a,b):
    if a< 5:
        return
    return a + b
num = input('Enter An Interger: ')

def sqare(num):
    if not num.isdigit():
        return 'invalid Entry'
    num = int(num)
    return num * num
print(num, 'Squared is:', square(num))