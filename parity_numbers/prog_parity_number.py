def parity(number):
	result = number % 2
	if result == 0:
		return 'Число ' + str(number) + ' чётное'
	return 'Число ' + str(number) + ' нечётное'

print(parity(496962))
