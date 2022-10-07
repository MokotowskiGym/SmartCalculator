scores = input().split()
# scores = "C C C I C C C C I I C C C C C C C C C".split()
# put your python code here
fails = 0
points = 0
for score in scores:
    if score == "C":
        points +=1
    else:
        fails +=1
    if fails == 3:
        break

if fails ==3:
    print ("Game over")
else:
    print("You won")

print(points)
