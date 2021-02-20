import curses
from random import randint

# setup screen window
curses.initscr()
janela = curses.newwin(20, 60, 0, 0)
janela.keypad(1)
curses.noecho() # no other input characters than keypad

curses.curs_set(0) # initial
janela.border(0)
janela.nodelay(1) # no waiting for user next key pressed

# snake and food
snake = [(4, 10), (4,9), (4,8)]

def endgame():
	curses.endwin()

def add_food(y, x):
	janela.addch(y, x, '#')

food = (10, 20)
add_food(food[0], food[1]) # comida inicial

SIDE_KEYS = [curses.KEY_LEFT, curses.KEY_RIGHT]

score = 0

ESC = 27
key = curses.KEY_RIGHT

while True:
	janela.addstr(0, 2, 'Score: ' + str(score) + ' ')
	janela.timeout(150 - (len(snake)) // 5 + len(snake)//10 % 120)
	
	prev_key = key

	# tecla teclada
	event = janela.getch()

	if event == ESC:
		endgame()

	key = event if event != -1 else prev_key
	
	if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
		key = prev_key

	y = snake[0][0]
	x = snake[0][1]
	if key == curses.KEY_DOWN:
		y += 1
	if key == curses.KEY_UP:
		y -= 1
	if key == curses.KEY_LEFT:
		x -= 1
	if key == curses.KEY_RIGHT:
		x += 1

	snake.insert(0, (y, x))

	# Se bateu na borda. 
	if y == 0: break
	if y == 19: break
	if x == 0: break
	if x == 59: break
	
	if (prev_key in SIDE_KEYS and key in SIDE_KEYS) and prev_key == key:
		pass
	else:
		# se snake in snake.
		if snake[0] in snake[1:]: break

	if snake[0] == food:
		score += 1
		food = ()
		while food == ():
			food = (randint(1, 18), randint(1,58))
			if food in snake:
				food = ()
		add_food(food[0], food[1])
	else:
		# retira ultimo item da cobra para 
		last = snake.pop()
		janela.addch(last[0], last[1], ' ')

	janela.addch(snake[0][0], snake[0][1], '*')

endgame()
print ('Final Score: %s' % score)


