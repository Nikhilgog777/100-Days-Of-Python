#  Use *args to write a sum_all() function that adds any number of arguments.

def sum_all( *args ):
    total = 0
    for number in args:
        total += number
    return total

sum1 = sum_all(45, 34, 65)

sum2 = sum_all(31, 87)

print(sum1)
print(sum2)
