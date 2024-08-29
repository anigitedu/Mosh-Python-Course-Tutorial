# i=1
# while i<=4:
#     print('*'*i)
#     i=i+1
# print("Done")
## Guessing game
# secret=6
# guesschance=3
# while guesschance>0:
#     guess=int(input('Enter your guess: '))
#     if guess==secret:
#         print('You won')
#         break
#     else:
#         guesschance=guesschance-1
#         print('You have '+str(guesschance)+' chances left')

## CAR GAME
inpte=(input(': '))
if inpte=='help':
    print('start - to start the car')
    print('stop - to stop the car')
    print('quit - to exit')
    action=(input(': '))
    if action=='start':
        print('Car started...Ready to go')
    elif action=='stop':
        print('Car stopped')
    elif action=='quit':
        print('Exiting...')
else: 
    print('I dont understand that')
