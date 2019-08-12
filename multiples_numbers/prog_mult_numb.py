while 1:
	print('Эта программа определяет и выводит числа кратные двум в заданом диапазоне.')
	input('Если понятно нажмите Enter. Иначе нажмите тоже Enter.')
	numb1 = input('Введите первое число: ')
	numb2 = input('Введите второе число: ')

	if not numb1.isdigit() or not numb2.isdigit():
		print('Ошибка! Введено неверное значение.')
	else:
		def multiples_number(start, finish):
			i = start
			res = ''
			while i <= finish:
				if i % 2 == 0:
					res = res + str(i) + ' кратно двум' + '\n'
				i += 1
			return res

		print(multiples_number(int(numb1), int(numb2)))




