import csv


def findout_length(file_path):
    with open("data.csv", "r") as our_file:
        read_it = csv.reader(our_file)
        reader_list = list(read_it)
        print(reader_list)
        return len(reader_list)
def append_to_csv(file_path, name, email):
    future_filed_names = ['id', 'name', 'email']
    #the number of the rows?
    next_id = findout_length(file_path)
    with open(file_path, "a") as our_file:
         writer = csv.DictWriter(our_file, fieldnames=future_filed_names)
         #writer.writeheader()
         writer.writerow({
            'id': next_id,
            'name': name,
            'email': email
            })
append_to_csv("data.csv", "Bohdan", "chillimillitilli@gmail.com")