unconfirmed_users = ['alice', 'brian', 'candace']
confirem_users = []
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	confirem_users.append(current_user)
	
print(confirem_users)
print(unconfirmed_users)
