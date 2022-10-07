three_months = input().split()
checkTpl = tuple(three_months)
check =False
for tpl in months:
        if checkTpl == tpl :
                check = True
        # else:
                # print (False)
print (check)
