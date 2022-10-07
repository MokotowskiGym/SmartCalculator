numbers = input().split()
anwsers = input().split()

answersSet = set(anwsers)
numbersSet = set(numbers)
fail = False
for number in numbers:
    if not number in answersSet:
        fail = True

for anwser in anwsers:
    if not anwser in numbersSet:
        fail = True

print (not  fail)

