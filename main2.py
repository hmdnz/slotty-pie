# packages imported to make symbols work with vs code
import sys
import io
import random

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def spin_row():
    symbols=['🍒', '🍉', '🍋', '🔔', '⭐']

    results = []

    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


# Advanced and concise way to spin row
# def spin_row():
#     symbols=['🍒', '🍉', '🍋', '🔔', '⭐']
#     return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print(" | ".join(row))

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
        
        bet = int(input('Place your bet amount: '))
        if bet <= 0:
                print("Bet amount must be greater than 0.")
                continue
        if bet > balance:
                print("Bet amount exceeds current balance.")
                continue
            
        balance -= bet  
        # Update balance (this is a placeholder, update according to game logic)
            
        row=spin_row()
        print('spining......\n')
        print_row(row)
        

if __name__ == '__main__':
    main()
