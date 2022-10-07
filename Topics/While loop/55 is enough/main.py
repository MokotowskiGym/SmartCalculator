a = 0
numbers = list()
while a != 55:
    a = int(input())
    if a != 55:
        numbers.append (a)
print  (len(numbers))
print (sum(numbers))
print  (sum(numbers)//len(numbers))
