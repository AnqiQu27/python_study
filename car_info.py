def make_car(manufacturer, kind, **info):
	car_info = {}
	car_info['company'] = manufacturer
	car_info['type'] = kind
	
	for key, value in info.items():
		car_info[key] = value
		
	return car_info
	
car = make_car('subaru', 'outback', color = 'blue', tow_pack_age = True)
print(car)
