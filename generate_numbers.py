from random import randint

count = 2 * 1000 * 1000 * 1000

for _ in range(count):
	value = randint(0,10)
	if value !=5 :
		print(value, end=" ")
	else:
		print(value)
