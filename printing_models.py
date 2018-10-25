unprinted_designs = ['iphone case', 'robot pendat', 'dodecahedron']
completed_models = []

def print_model(unprinted, printed):
	while unprinted:
		current = unprinted.pop()
		printed.append(current)
		
def show_completed(printed):
	for model in printed:
		print(model)
		
print_model(unprinted_designs, completed_models)
show_completed(completed_models)
	
		
	
