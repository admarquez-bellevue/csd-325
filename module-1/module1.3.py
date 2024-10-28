
def countdown():
    bottles = int(input('How many bottles of beer are there? '))
    while bottles >= 1:
        if bottles != 1:
            print(bottles, 'bottles of beer on the wall,', bottles, 'bottles of beer.')
            print('Take one down, pass it around,', bottles -1, 'bottles of beer on the wall.')
            print()
        if bottles == 1:
            print('1 bottle of beer on the wall, 1 bottle of beer.')
            print('Take one down, pass it around, no more bottles of beer on the wall.')
            print()
            print('You are out of beer. Go to the store and buy some more.')
        bottles -= 1
    
    while True:
        num = int(input('Enter 0 to exit program: '))
        if num == 0:
            print('>> Program ended using exit code 0')
            print()
            break

countdown()