import csv, time

transactions = open('transactions.csv')
reader = csv.reader(transactions)

transactionsConverted = open('transactionsConverted.csv', 'w')
writer = csv.writer(transactionsConverted)

# Write header row
writer.writerow(['Date','Payee','Category','Memo','Outflow','Inflow'])

for row in reader:
	date = time.strftime('%d/%m/%Y', time.strptime(row[0], '%d-%m-%Y')) # DD/MM/YYYY
	payee = row[4]
	category = ''
	memo = row[7]

	# Check if the transaction is 'Debet' (outflow) or 'Credit' (inflow)
	if row[3] == 'Debet':
		outflow = row[2]
		inflow = '0'
	elif row[3] == 'Credit':
		outflow = '0'
		inflow = row[2]

	writer.writerow([date, payee, category, memo, outflow, inflow])

transactionsConverted.close()