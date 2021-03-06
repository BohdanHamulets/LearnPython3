import csv
import datetime
import shutil
import os
from tempfile import NamedTemporaryFile


#file_ = 'utils/template/email_message.txt'
#file_item_path = os.path.join(os.path.dirname(__file__), file_)
#filename = file_path

file_item_path = os.path.join(os.path.dirname(__file__), "data.csv")


def read_data(user_id=None, email=None):
    filename = file_item_path
    print(filename)
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