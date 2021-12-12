import sys
file_name = sys.argv[1]
with open(file_name,'r') as f:
    lines = f.readlines()
    hor_pos = 0
    depth = 0 
    aim = 0
    for line in lines:
        direction, val = line.strip('\n').split(' ')
        if direction == 'forward':
            hor_pos = hor_pos + int(val)
            depth = depth + (aim * int(val))
        elif direction == 'down':
            aim = aim + int(val)
        elif direction == 'up':
            aim = aim - int(val)
    print(hor_pos * depth)