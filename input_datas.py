def get_data():
	print("Enter one number each time, enter 'end' anytime to end input")
	datas = []
	data = ''
	while data != 'end':
		data = input('data = ')
		try:
			data = float(data)
		except ValueError:
			if data != 'end':
				print('invalid input')
			continue
		datas.append(data)
	return datas
	
