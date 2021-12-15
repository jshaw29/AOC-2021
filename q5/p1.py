import sys
from grid import Grid
def load_data():
    filename = sys.argv[1]
    f = open(filename, 'r')
    lines  = f.readlines()
    data = [(int(cord.split(',')[0]),int(cord.split(',')[1])) for line in lines for cord in line.split(' -> ')]
    vectors =[]
    max_x, max_y = [0,0]
    for i in range(0, len(data),2):
        vectors.append([data[i],data[i+1]])
        if data[i][0] > max_x or data[i+1][0] > max_x:
            max_x = max(data[i][0], data[i+1][0])
        if data[i][1] > max_y or data[i+1][1] > max_y:
            max_y = max(data[i][1], data[i+1][1])

    return max_x, max_y,vectors

if __name__ =='__main__':
    max_x, max_y, vectors = load_data()
    print(max_x, max_y)
    grid = Grid(max_x=max_x, max_y=max_y)
    grid.print()
