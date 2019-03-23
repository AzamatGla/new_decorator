import re

def decorator(f):
    def wrapper(x):
        print('original mobile number: ')
        f(x)

        if len(x) == 13:
            return num
        elif len(x) == 12:
            return '+'+num
        elif len(x) == 11:
            x1 = re.sub('0','+91', x)
            return x1
        else:
            pass
    return wrapper

@decorator
def mobile_numbers(num):
    print(num)


num = input('Please enter your mobile number: ')
print(mobile_numbers(num))


