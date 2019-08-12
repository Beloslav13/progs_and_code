# Узнаем среднее значение возраста
nadya = ('Nadya', 'Belyaninova', 22)
vlad = ('Vlad', 'Zvyagintsev', 23)
rada = ('Rada', 'Beagle', 1)
sema = ('Sema', 'York', 7)
fred = ('Fred', 'Efremov', None)
da = ('Ras', 'Ef', None)

old = 'Возраст выше среднего'
young = 'Возраст ниже среднего'

d = 0
e = 0
template = '{} - {}'

for i in nadya, vlad, rada, sema, fred:
	# Обозначаем условие, для того чтобы не схватить ошибку если возраст окажется None
	if i[2] == None:
		continue
	# Суммируем возраст
	d = d + i[2]
	# Считаем кол-во элементов в кортеже у которых присутствует возраст, для того чтобы узнать среднее значение
	e += 1
	if i[2] > 8:
		print(template.format(i[0], old.lower()))
	else:
		print(template.format(i[0], young.lower()))

result = d / e
print(result)
