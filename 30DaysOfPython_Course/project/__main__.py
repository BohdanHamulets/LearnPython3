from argparse import ArgumentParser
from data_manager import read_data
from utils.templates import get_template, adjust_string

parser = ArgumentParser(prog="project")
parser.add_argument("type", type=str, choices=['view', 'message'])
parser.add_argument('-id', '--user_id', type=int)
parser.add_argument('-e', '--email', type=str)
args = parser.parse_args()

#print(args)
#print(args.user_id)
print(read_data(user_id=args.user_id, email=args.email))



if args.type =="view":
    print(read_data(user_id=args.user_id))
    print(read_data(email=args.email))
elif args.type == "message":
    file_ = 'utils/template/email_message.txt'
    file_html = 'utils/template/email_message.html'
    template_content = get_template(file_)
    template_content_html = get_template(file_html)
    context = {
        "insert_name": "Bohdan",
        "insert_total":55.3,
        "insert_date":"27/11/2017"
    }


print(adjust_string(template_content, context))
print(adjust_string(template_content_html, context))

