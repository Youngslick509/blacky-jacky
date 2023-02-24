import random

deck = list(range(2, 10)) * 4
deck += [10] * 4 *4
random.shuffle(deck)
player = deck.pop(0)
dealer = deck.pop(0)
while player < 21 and dealer < 17:

    print(f'Player has {player} \ndealer has {dealer}')
    if input('Do you want to draw another card?:') == 'y':
        player += deck.pop(0)
    dealer += deck.pop(0)

# put code to check who won        
if player < 21 and dealer > 21:
    print('player winssssssssssssssssssssssssssssssss👍')
elif player > 21 and dealer < 21:
    print('dealer winssssssssssssssssssssssssssssssss👍')
elif player > dealer:
    print('player winssssssssssssssssssssssssssssssss👍')
elif player < dealer:
    print('dealer winssssssssssssssssssssssssssssssss👍')
else:
    print('tie')