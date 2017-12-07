import csv

with open("data.csv", "w+") as csvfilenew:
    writer = csv.writer(csvfilenew)
    writer.writerow(["Tilte", "Description"])
    writer.writerow(["Row1", "Some decs"])

#This will wrire and override
# - - - - - - - - - - - - - - - - - - 

with open("data.csv", "a") as csvfilenew:
    writer = csv.writer(csvfilenew)
    writer.writerow(["New", "Stuff"])

#this will append (notice 'a' instead of 'w') - info about this
#can be found in docs python cvs 
# - - - - - - - - - - - - - - - - - - - - - 

with open("data.csv", "r") as bla:
    displayer = csv.reader(bla)
    for whatever in displayer:
        print(whatever)

#this will read and display the data in list format
# - - - - - - - - - - - - - - - - - - - - - - - - 


with open("data.csv", "r") as bla:
    displayer = csv.DictReader(bla)
    for whatever in displayer:
        print(whatever)

#this will read and display the data in dictionary format
# - - - - - - - - - - - - - - - - - - - - - - - - 

with open("data.csv", "a") as our_file:
    future_filed_names = ["id", "Name"]
    writer = csv.DictWriter(our_file, fieldnames=future_filed_names)
    writer.writerow({"id":1,"Name":"Soap"})
    for whatever in our_file:
        print(whatever)