def build_profile(first, last, **user_info):
	''' create a dict to store the info of users '''
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
