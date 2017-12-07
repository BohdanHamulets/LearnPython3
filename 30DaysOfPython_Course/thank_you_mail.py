import datetime

database_names = ["Justin", "John", "Veronika", "Irvin", "Bohdan",]
database_amounts = [123.6511, 577.2222, 25, 3669.211, 755.3111111,]
database_date = ["03/05/17", "07/07/2017", "25/9/13", "25/12/07", "27/10/17",]

database_message = """Hi {insert_name}!
Thanks you for your purchase on {insert_date}.
Purchase total was ${insert_total}.  
We really appreciate everyone of our customers,
and hope you've enjoy it!

Thank you! :)
"""

def make_mails(names, amouts):
	#message = []
	if len(names) == len(amouts):
		i = 0
		z = 0
		today = datetime.datetime.today()
		date_text = "{today.month}/{today.day}/{today.year}".format(today=today)
		for name in names:
			#This if prints current date or takes date from "database_date" string
			#just for fun :)
			if z % 2 == 0:
				insert_date1 = date_text
			else:
				insert_date1 = database_date[z]
			grasefull_price = "%.2f" %(database_amounts[i])
			new_message = database_message.format(
				insert_name = name,
				insert_total = grasefull_price,
				insert_date = insert_date1
				)
			i += 1
			z += 1
			print(new_message)

make_mails(database_names, database_amounts)


