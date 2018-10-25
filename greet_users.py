def greet_users(names):
	''' greet people in the lists '''
	for name in names:
		msg = 'hello ' + name.title()
		print(msg)
		
usernames = ['hanabi', 'uzi', 'luo']
greet_users(usernames)
