

def readInput(filename='test11.in'):
    """
    read input file
    :param filename: filename
    :return: an array of testcases, each testcase is an array of numbers
    """
    f = open(filename, 'r')
    f.readline()
    lines = f.readlines()
    inp = []
    for i in range(0, len(lines), 2):
        a = (map(lambda x: int(x), lines[i].split(' ')), map(lambda x: int(x), lines[i+1].split(' ')))
        inp += [a, ]
    return inp


def solve(a):
    """
    solve the problem
    :param a: an array of input numbers
    :return: output array that has been removed duplicated numbers
    """
    pts = a[0]
    goals = a[1]
    merge = zip(a[0], a[1])
    hit = map(lambda d: d[0]>=d[1], merge)
    best_streak = 0
    streak = 0
    for i in range(len(hit)):
        if hit[i]:
            streak += 1
            if streak > best_streak:
                best_streak = streak
        else:
            streak = 0
    return best_streak


def writeOutput(results, filename='test11.out'):
    """
    write output file
    :param filename: filename
    :return: write results to file
    """
    lines = map(lambda result: str(result), results)
    f = open(filename, 'w')
    f.write('\n'.join(lines))
    f.close()


def main():
    testcases = readInput()
    results = map(lambda testcase: solve(testcase), testcases)
    writeOutput(results)


if __name__=='__main__':
    main()