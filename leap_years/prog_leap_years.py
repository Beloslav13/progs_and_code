year = 2019
template = '{} {}. {}'

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print(template.format(str(year), 'год высокосный', 'Выполнилось условие: year % 400 == 0'))
		else:
			print(template.format(str(year), 'год обычный', 'Выполнилось условие: year % 400 != 0'))
	else:
		print(template.format(str(year), 'год высокосный', 'Выполнилось условие: year % 100 != 0'))
else:
	print(template.format(str(year), 'год обычный', 'Выполнилось условие: year % 4 != 0'))





