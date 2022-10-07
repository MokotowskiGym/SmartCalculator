str = input()
subStr = "old"
l = str.find((subStr))
r = str.rfind((subStr))
print( max(l, r))
