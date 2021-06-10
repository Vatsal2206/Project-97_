guess = 5
lives = 4

while lives >= 0 :
    print('PLEASE GUESS A NUMBER BETWEEN 0 and 9!')
    inputNumber = int(input('Please enter your guess here! :'))

    if(inputNumber == guess):
        print('CONGRATULATIONS! You won')
        break

    elif(inputNumber < guess):
        print('Guess a number more than ', inputNumber)
        print('You have ',lives, ' chances left!')

    elif(inputNumber > guess):
        print('Guess a number less than ', inputNumber)
        print('You have ',lives, 'chances left!')
    
    else:
        print('Please enter a number between 0 and 9!')

    lives = lives - 1

if(lives == -1):
    print('You lost!! The number was ', guess)