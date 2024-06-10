import sys
import io
import random

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print('***********')
    print("   |   ".join(row))
    print('***********')

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 25
        return 0
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
        except ValueError:
            print("Invalid input. Please enter a valid bet amount.")
            continue
        
        if bet <= 0:
            print("Bet amount must be greater than 0.")
            continue
        if bet > balance:
            print("Bet amount exceeds current balance.")
            continue
            
        balance -= bet
        # Update balance (this is a placeholder, update according to game logic)
        
        row = spin_row()
        print('spinning......\n')
        print_row(row)
        
        payout=get_payout(row,bet)
        
        if payout > 0:
            print(f'You won ${payout}')
        else:
            print('Sorry you lost this round')
        balance += payout
        
    print("Game over. You have run out of balance.")

if __name__ == '__main__':
    main()
