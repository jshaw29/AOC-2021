import sys
filename = sys.argv[1]
boats = dict()
with open(filename, 'r') as f:
    lines = f.readlines()
    lines = list(map(lambda x: int(x.strip('\m')), lines))
    print(lines)
    sums = []
    prev_sum = 0
    count =0
    for idx, val in enumerate(lines):
        curr_sum = 0
        if idx +1 < len(lines) and idx+2 < len(lines):
            curr_sum = val + lines[idx+1] + lines[idx+2]
        if prev_sum != 0:
            count = count + (1 if curr_sum > prev_sum else 0)
        prev_sum = curr_sum
    print(count)