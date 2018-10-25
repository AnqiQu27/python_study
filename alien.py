alien_0 = {'x_pos' : 0, 'y_pos' : 25, 'speed' : 'medium'}

if alien_0['speed'] == 'medium':
	alien_0['x_pos'] = alien_0['x_pos'] + 2
else:
	alien_0['x_pos'] = alien_0['x_pos'] + 3
	
print(alien_0)

del alien_0['speed']
print(alien_0)

