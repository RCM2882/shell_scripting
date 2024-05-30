import random

def gametime():
    print("It's time to start the game!")
    choices = ['rock', 'paper', 'scissors']

    while True:
        user_choice = input('What do you choose: rock, paper, or scissors: ').lower()
        if user_choice not in choices:
            print('This is not an option. Pick rock, paper, or scissors.')
            continue

        competing_choice = random.choice(choices)
        print(f'The computer chooses: {competing_choice}')

        if user_choice == competing_choice:
            print('Tie Game!')
        elif (user_choice == 'paper' and competing_choice == 'rock') or \
             (user_choice == 'scissors' and competing_choice == 'paper') or \
             (user_choice == 'rock' and competing_choice == 'scissors'):
            print('You are the winner')
        else:
            print('The computer beat you')

        another_game = input('Do you want to play another round? yes or no: ').lower()
        if another_game != 'yes':
            print('It was fun competing against you!')
            break 


if __name__ == "__main__":
    gametime()


