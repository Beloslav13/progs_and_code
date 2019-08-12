from colorama import Fore, Back, Style
print(Back.CYAN)

while 1:
	print('Программа калькулятор запущена')
	print('Пожалуйста следуйте инструкциям ниже.')
	do = input('Что нужно сделать? (+, -, *, /): ')

	number_one = float(input('Введите первое число: '))
	number_two = float(input('Введите второе число: '))
	print(Fore.WHITE)
	print(Back.GREEN)

	if do == '+':
		result = number_one + number_two
		print('Результат: ' + str(result))

	elif do == '-':
		result = number_one - number_two
		print('Результат: ' + str(result))

	elif do == '*':
		result = number_one * number_two
		print('Результат: ' + str(result))

	elif do == '/':
		result = number_one / number_two
		print('Результат: ' + str(result))

	else:
	    print('Выбрана неверная операция')


	a = input('Нажмите Enter для выхода')
	print('Программа завершена.')
