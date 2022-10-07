from collections import Counter


shopping_list = ['carrots', 'carrots', 'bread', 'tomatoes', 'onions', 'apples', 'tomatoes', 'carrots',
          'tomatoes', 'onions', 'onions', 'onions', 'bread', 'milk', 'bread', 'apples']

# shopping_list = input().split()
# ct = Counter(shopping_list).items()
# for item in ct:
#     print(item)
#     print (ct[item])
#
# print (type(ct))
# ctt = {}
# print (type(ctt))


dict = {}
for item in shopping_list:
    if item in dict:
        dict[item]= dict[item]+1
    else:
        dict[item] = 1


for item, count in dict.items():
    print (item , count)
