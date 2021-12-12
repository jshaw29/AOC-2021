import sys

def load_data():
    fileanme = sys.argv[1]
    with open(fileanme, 'r') as f:
        lines = [x for x in f.readlines() if x!='\n']
        moves = [int(x) for x in lines[0].strip('\n').split(',')]
        del lines[0]
        print(lines)
        boards =[]
load_data()