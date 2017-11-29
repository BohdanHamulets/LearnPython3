from argparse import ArgumentParser
from data_manager import read_data


parser = ArgumentParser(prog="project")
parser.add_argument('-id', '--user_id', type=int)
parser.add_argument('-e', '--email', type=str)
args = parser.parse_args()

print(args)
#print(args.user_id)
print(read_data(user_id=args.user_id, email=args.email))
