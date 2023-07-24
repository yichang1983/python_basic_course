# print(num)      # name 'num' is not defined
# print(1/0)        # division by zero

try:
    print(1/0)
except (NameError, ZeroDivisionError) as result:
    print(result)
