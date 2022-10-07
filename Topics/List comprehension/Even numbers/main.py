# the following line reads the list from the input; do not modify it, please
def isEven(myInt)-> bool:
    if myInt % 2 == 0:
        return True
    else:
        return False




my_numbers = [int(x) for x in input().split(" ")]
evenNumbers = [number for number in my_numbers if isEven(number)]
# work with the variable 'my_numbers'

print (evenNumbers)
