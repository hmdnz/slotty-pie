# packages imported to make symbols work with vs code
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def spin_row():
    pass

def print_row():
    pass

def get_payout():
    pass

def main():
    balance = 100
    
    print('**************************')
    print('  Welcome to python slots ')
    print('  Symbols: 🍒 🍉 🍋 🔔 ⭐  ')
    print('**************************')
    
    while balance > 0:
        print(f'Current Balance: ₦{balance}')
        try:
            bet = int(input('Place your bet amount: '))
            if bet <= 0:
                print("Bet amount must be greater than 0.")
                continue
            if bet > balance:
                print("Bet amount exceeds current balance.")
                continue
            balance -= bet  # Update balance (this is a placeholder, update according to game logic)
        except ValueError:
            print("Invalid input. Please enter a valid bet amount.")

    print("Game over. You have run out of balance.")

if __name__ == '__main__':
    main()
