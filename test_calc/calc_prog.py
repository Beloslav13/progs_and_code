from colorama import init
from colorama import Fore, Back, Style
init()

while True:
	print(Fore.GREEN)
	print('Программа запущена.\nСледуйте инструкциям на экране.')
	print(Fore.CYAN)
	number_one = input('Введите первое число: ')
	number_two = input('Введите второе число: ')
	do = input('Введите операцию(+, -, /, *): ')

	if (number_one.isdigit() and number_two.isdigit()) or (float(number_one) and float(number_two)):
		try:
			print(Fore.MAGENTA)
			if do == '+':
				result = float(number_one) + float(number_two)
				print(f'Результат: {result}')

			elif do == '-':
				result = float(number_one) - float(number_two)
				print(f'Результат: {result}')

			elif do == '/':
				result = float(number_one) / float(number_two)
				print(f'Результат: {float(result)}')

			elif do == '*':
				result = float(number_one) * float(number_two)
				print(f'Результат: {result}')

			else:
				print(Fore.RED)
				print('Вы ввели неверное значение или операцию!')

		except ZeroDivisionError:
			print(Fore.RED + 'Эй, на 0 делить нельзя!')
	else:
		try:
			pass
		except ValueError:
			print(Fore.RED)
			print('Вы ввели неверное значение или операцию!')
	print(Fore.GREEN + 'Программа завершена.')
