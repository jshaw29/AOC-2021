import sys
file_name = sys.argv[1]
with open(file_name,'r') as f:
    lines = f.readlines()
    hor_pos = 0
    depth = 0 
    for line in lines:
        direction, val = line.strip('\n').split(' ')
        print(direction, val)
        if direction == 'forward':
            hor_pos = hor_pos + int(val)
        elif direction == 'down':
            depth = depth + int(val)
        elif direction == 'up':
            depth = depth - int(val)
        print(hor_pos, depth)
    print(hor_pos * depth)