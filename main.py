import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winning(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                break
        else:
            winnings += values[symbol] * bet
            print(f"You won ${values[symbol] * bet} on line {line + 1} with symbol '{symbol}'.")
    return winnings

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count): 
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i < len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("Enter the amount you deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(f"\nPlease enter a positive amount.")
        else:
            print(f"\nInvalid input. Please enter a numeric value.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("Invalid input. Please enter a numeric value.")
    return lines

def get_bet():
    while True:
        bet = input(f"Enter the amount per line you would like to bet?: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please enter a bet between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Invalid input. Please enter a numeric value.")
    return bet 

def spin(amount_deposited):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > amount_deposited:
            print(f"\nYou do not have enough funds to place this bet. Your current balance is ${amount_deposited}.")
            print(f"Your total bet of ${total_bet} exceeds your balance.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines, your total bet is ${total_bet}.")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings = check_winning(slots, lines, bet, symbol_value)
    return winnings - total_bet
    

def main():
    print("Welcome to the Slot System!")
    amount_deposited = deposit()
    while True:
        print(f"\nYour current balance is ${amount_deposited}.")
        if amount_deposited <= 0:
            print("You have no funds left. Please deposit more money to continue playing.")
            break
        winnings = spin(amount_deposited)
        amount_deposited += winnings
        if winnings > 0:
            print(f"You won ${winnings}! Your new balance is ${amount_deposited}.")
        else:
            print(f"You lost ${-winnings}. Your new balance is ${amount_deposited}.")
        
        if input("Do you want to play again? (y/n): ").lower() != 'y':
            break
    print(f"Thank you for playing! Your final balance is ${amount_deposited}.")
    
main()