import csv
import datetime
import shutil
from tempfile import NamedTemporaryFile


def read_data(user_id=None, email=None):
    filename = "data.csv"
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        items = []
        for row in reader:
            if user_id is not None:
                if int(user_id) == int(row.get("id")):
                    return row
            if email is not None:
                if email == row.get("email"):
                    return row
        return "{user_id} or {email} not found".format(user_id=user_id, email=email)


def get_length(file_path):
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)

def append_data(file_path, name, email, amount):
    fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
    #the number of rows?
    next_id = get_length(file_path)
    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
                "id": next_id,
                "name": name,
                "email": email,
                "sent": "",
                "amount": amount,
                "date": datetime.datetime.now()
            })

append_data("data.csv", "Justin", "hello@teamcfe.com", 123.22)

def edit_data(edit_id=None, email=None, amount=None, sent=None):
    filename = "data.csv"
    temp_file = NamedTemporaryFile(delete=False)

    with open(filename, "rb") as csvfile, temp_file:
        reader = csv.DictReader(csvfile)
        fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            #print(row['id'] == 4)
            if edit_id is not None:
                if int(row['id']) == int(edit_id):
                    row['amount'] = amount
                    row['sent'] = sent
            elif email is not None and edit_id is None:
                if str(row['email']) == str(email):
                    row['amount'] = amount
                    row['sent'] = sent
            else:
                pass
            writer.writerow(row)
        
        shutil.move(temp_file.name, filename)
        return True
    return False


#edit_data(8, 9992.32, "")
edit_data(email='hello@teamcfe.com', amount=99.99, sent='')