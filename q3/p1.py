import sys
filename = sys.argv[1]
gamma_rate = ''
def get_most_common(arr, pos):
    ls = list(map(lambda x: int(x[pos]),arr))
    count = 0
    for i in ls:
        count = count + (1 if i == 1 else -1 )
    return "1" if count > 0 else "0"

with open(filename, 'r') as f:
    a = "10000"
    lines  = f.readlines()
    lines = list(map(lambda x: x.strip('\n'), lines))
    for i in range(0, len(lines[0])):
        gamma_rate = gamma_rate + get_most_common(lines, i)
    ep_rate = ''.join(['1' if i == '0' else '0' for i in gamma_rate])
    gamma_rate = int(gamma_rate,2)
    ep_rate = int(ep_rate,2)
    # ep_rate = ~gamma_rate & 0b011111
    print(gamma_rate)
    print(ep_rate)
    print(gamma_rate*ep_rate)

