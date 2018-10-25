my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods1 = my_foods[:]
friend_foods1.append('egg')
friend_foods2 = my_foods
friend_foods2.append('egg')
print(friend_foods1)
print(my_foods)

print('The first three items are:' + str(my_foods[ : 3]))
print('The last three items are:' + str(my_foods[-3 : ]))
