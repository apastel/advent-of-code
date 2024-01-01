from advent.load import read_input
from time import perf_counter as pc

def find_matches(winning_numbers, my_numbers):
    return set(winning_numbers) & set(my_numbers)

def calculate_points(matches):
    return 2 ** (len(matches) - 1) if matches else 0

cards = [[card] for card in read_input(group=True)[0]]
total_cards = 0
start_time = pc()
for card_set in cards:
    for card in card_set:
        total_cards += 1
        card_number = int(card[card.find(" "):card.find(":")])
        winning_numbers = [int(num) for num in card[card.find(":")+1:card.find("|")].strip().split(" ") if num]
        my_numbers = [int(num) for num in card[card.find("|")+1:].strip().split(" ") if num]
        
        num_matches = len(find_matches(winning_numbers, my_numbers))
        for x in range(card_number, card_number + num_matches):
            cards[x].append(cards[x][0])

print(f"There are now {total_cards} cards in total.")
print(f"That took {pc() - start_time} seconds, big whoop.")