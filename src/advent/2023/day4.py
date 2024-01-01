from advent.load import read_input

def find_matches(winning_numbers, my_numbers):
    return set(winning_numbers) & set(my_numbers)

def calculate_points(matches):
    return 2 ** (len(matches) - 1) if matches else 0

data = read_input(group=True)[0]
total_points = 0
for card in data:
    card_number = int(card[card.find(" "):card.find(":")])
    winning_numbers = [int(num) for num in card[card.find(":")+1:card.find("|")].strip().split(" ") if num]
    my_numbers = [int(num) for num in card[card.find("|")+1:].strip().split(" ") if num]
    
    card_matches = find_matches(winning_numbers, my_numbers)
    card_points = calculate_points(card_matches)
    total_points += card_points
    print(f"Card {card_number} has {len(card_matches)} winning numbers, so it is worth {card_points} points.")

print(f"The scratchcards are worth {total_points} points in total.")