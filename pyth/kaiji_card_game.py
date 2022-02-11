import random

WEAKNESSES = {'Slave': 'Citizen', 'Citizen': 'King', 'King': 'Slave'}

while input('enter 1 to play, press any buttont o end: ') == '1':
	side = random.randrange(0, 2)
	player_hand = ['King' if side else 'Slave', *(['Citizen'] * 4)]
	opponent_hand = ['Slave' if side else 'King'] + player_hand[1 :]

	print('you have king' if side else 'you have homeless')
	while player_hand:
		player_choice = int(input(
			'ur options: ' + '\t'.join(
				f'({i}) {card} ' for i, card in enumerate(player_hand)
			)
		))

		assert player_choice in range(len(player_hand)), "Not a valid move"
		player_move = player_hand[player_choice]
		
		rand = random.randrange(len(opponent_hand))
		opp_play = opponent_hand[rand]

		print(f'Your move: {player_move}\tYour opponent move: {opp_play}\n')
		if WEAKNESSES[player_move] == opp_play:
			print('You lost')
			break
		elif WEAKNESSES[opp_play] == player_move:
			print('you won')
			break

		player_hand.pop(player_choice)
		opponent_hand.pop(rand)
