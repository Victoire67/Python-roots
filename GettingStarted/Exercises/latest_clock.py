from itertools import permutations


def latest_clock(a,  b, c, d):

    digits = [str(a), str(b), str(c), str(d)]

    all_permutations = [list(item) for item in list(permutations(digits))]


    all_valid_clocks = [item for item in all_permutations if  int(item[0] + item[1]) <= 23 and int(item[2] + item[3]) <= 59]


    all_valid_clocks.sort()

    print(all_valid_clocks[-1])

    valid_clock = all_valid_clocks[-1]

    result = f"{valid_clock[0]}{valid_clock[1]}:{valid_clock[2]}{valid_clock[3]}"

    print(result)

    return result