class ExppressionPart:
    def __init__(self, str):
        self.ok = isCalculable(str)
        self.int = rectifyExpression(str)

def isCalculable(str) ->bool:
    nChr = 0
    properexpressionsStarted = False
    for chr in str:
        if not chr in "1234567890+-":
            return False
            break
        nChr +=1
    return True

def rectifyExpression(expr) ->int:
    strLen = len(expr)
    newStr = ""
    minuses = 0

    for n  in range(0 , strLen):
        current = expr[n:n + 1]
        if current == "+":
            pass
        elif current == "-":
            minuses += 1
        else:
            newStr +=current
    if newStr == "":
        newStr = str(0)
    if not isEven(minuses):
        newStr = "-" + newStr

    return  int(newStr)

def isEven(number) ->bool:
    if number%2 == 0:
        return True
    else:
        return  False


expressionPart = ExppressionPart(str(55))
print (expressionPart.ok)

while True:
    expressionsStr = input()
    # expressionsStr = " -2 + 4 - 5 + 6"

    if expressionsStr == "/exit":
        break
    elif expressionsStr == "/help":
        print ("The program calculates the sum of expressions")
    elif expressionsStr == "":
        pass
    else:

        expressionsArr = expressionsStr.split()
        expressionsArrMod = [rectifyExpression(i) for i in expressionsArr]
        print (sum(expressionsArrMod))

print ("Bye!")



