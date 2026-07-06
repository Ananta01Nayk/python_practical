n = 0

try:
    result = 10/n
except ZeroDivisionError:
    print('cant division by zero')
finally:
    print('try it next time')