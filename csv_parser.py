import csv

class Parser:

	def csv_parse():
		total_spent = 0.0
		total_earned = 0.0
		with open('Example Statement.csv') as file:
			reader = csv.DictReader(file)
			for column in reader:
				amount = float(column['Amount'])
				if amount < 0:
					total_spent += amount
				elif amount > 0:
					total_earned += amount

		print(f'Total Earned this month: {round(total_earned, 2)}')
		print(f'Total Spent this month: {round(total_spent, 2)}')

Parser.csv_parse()