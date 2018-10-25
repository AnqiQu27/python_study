current_users = ['a', 'b', 'c', 'd', 'e']
new_users = ['f', 'g', 'a']
for user in new_users:
	if user in current_users:
		print('you cannot use this name')
	else:
		print('this name is ok')
			
