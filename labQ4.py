userinput=int(input('''Enter any (1,2 or 3 digit) number :'''))
for x in range(1,1000):
    if userinput % x ==0:
        print(x)