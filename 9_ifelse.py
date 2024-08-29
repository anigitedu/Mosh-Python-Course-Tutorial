ishot=True

if ishot & False:
    print('drink water')
else:
    print('drink soda')

inc=input('Enter your income: ')
creditscore=input('Enter you credscore: ')
if int(inc)>1000 and int(creditscore)>620 :
    print('You can have loan')
else:
    print('Try next time')