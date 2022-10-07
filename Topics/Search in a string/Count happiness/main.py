
str = input()
# str = "If you're happy and you know it, clap your hands If you're happy and you know it, clap your hands If you're happy and you know it, then your face will surely show it If you're happy and you know it, clap your hands If you're happy and you know it, stomp your feet If you're happy and you know it, stomp your feet If you're happy and you know it, then your face will surely show it If you're happy and you know it, stomp your feet If you're happy and you know it, shout 'Hurray!' (Hurray!) If you're happy and you know it, shout 'Hurray!' (Hurray!) If you're happy and you know it, then your face will surely show it If you're happy and you know it, shout 'Hurray!' (Hurray!) If you're happy and you know it, do all three (hurray!) If you're happy and you know it, do all three (hurray!) If you're happy and you know it, then your face will surely show it If you're happy and you know it, do all three (hurray!)"
substr = "happy"
substrLen = len(substr)
count = 0
for i in range(0, len(str) - substrLen):
    part = str[i:i+substrLen]
    if part == substr:
        count +=1

print (count)
