import sys
filename = sys.argv[1]
def get_most_common(arr, pos):
    ls = list(map(lambda x: int(x[pos]),arr))
    count = 0
    for i in ls:
        count = count + (1 if i == 1 else -1 )
    if count == 0:
    return "0" if count >= 0 else "1"

def get_least_common(arr,pos):
    ls = list(map(lambda x: int(x[pos]),arr))
    count = 0
    for i in ls:
        count = count + (1 if i == 1 else -1 )
    if count == 0:
    return "1" if count >= 0 else "0"

with open(filename, 'r') as f:
    a = "10000"
    lines  = f.readlines()
    lines = list(map(lambda x: x.strip('\n'), lines))
    oxy_lines = lines
    co2_lines = lines
    for i in range(0, len(lines[0])):
        most_common = get_most_common(oxy_lines, i)
        least_common = get_least_common(co2_lines,i)
        if len(oxy_lines) >1:
            oxy_lines = [x for x in oxy_lines if x[i] == most_common]
        if len(co2_lines) > 1:
            co2_lines = [x for x in co2_lines if x[i] == least_common]
    oxy_rating = int(oxy_lines[0],2)
    co2_rating = int(co2_lines[0],2)
    print(oxy_rating,co2_rating)
    print(co2_rating * oxy_rating)

    # ep_rate = ''.join(['1' if i == '0' else '0' for i in gamma_rate])
    # gamma_rate = int(gamma_rate,2)
    # ep_rate = int(ep_rate,2)
    # # ep_rate = ~gamma_rate & 0b011111
    # print(gamma_rate)
    # print(ep_rate)
    # print(gamma_rate*ep_rate)

