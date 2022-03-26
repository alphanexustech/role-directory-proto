import sys
from pprint import pprint

from helpers import file_processing
from src import lookup_merge

def main():
    # IDEA: Add a CLI to provide the 'file_path' for the directory as an input
    # IDEA: Add logic to default to 'default_file_path' if 'file_path' no input file_path from command line
    file_path = './test_data'

    # Load
    names = file_processing.read_file_names(file_path)
    dir_data = [] # The data from the 'file_path' directory
    # OPTIMIZE: Make this faster! Ask the Corvid, if needed ;)
    for file_name in names:
        d = file_processing.read_from_json(file_name)
        dir_data.append(d)

    # Merge
    merged = lookup_merge.merge_role_json(dir_data)
    file_processing.write_to_json('lookup', merged)

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
