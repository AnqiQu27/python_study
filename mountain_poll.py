responses = {}

polling_active = True

while polling_active:
	name = input('please input your name: ')
	response = input('please input your response: ')
	
	responses[name] = response
	
	repeat = input('is there anyone who want to express himself? yes/no ')
	if repeat == 'no':
		polling_active = False
		
for name, response in responses.items():
	print(name + ":" + response)
	
	
