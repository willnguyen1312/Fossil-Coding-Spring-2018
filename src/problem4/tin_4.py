

def readInput(filename='test3.in'):
    """
    read input file
    :param filename: filename
    :return: an array of testcases, each testcase is an array of numbers
    """
    f = open(filename, 'r')
    t = int(f.readline())
    testcases = []
    for i in range(t):
        x, y, n = map(int, f.readline().split(' '))
        a = map(lambda x: int(x[0:2])*60+ int(x[3:5]), f.readline().strip().split(' '))
        testcases.append({
            'x': x,
            'y': y,
            'a': a,
        })
    return testcases


def solve(a):
    """
    solve the problem
    :param a: an array of input numbers
    :return: output array that has been removed duplicated numbers
    """
    alarms = {}
    for alarm in a['a']:
        alarms[alarm] = alarms.get(alarm, 0) + 1
        alarms[alarm+a['y']-1] = alarms.get(alarm+a['y'] - 1, 0) - 1
    c = 0
    for i in sorted(alarms.keys()):
        c += alarms.get(i, 0)
        if c >= a['x']:
            return '%02d:%02d' % (i/60, i%60)
    return 'can not awake!'


def writeOutput(results, filename='test3.out'):
    """
    write output file
    :param filename: filename
    :return: write results to file
    """
    lines = results
    f = open(filename, 'w')
    f.write('\n'.join(lines))
    f.close()


def main():
    testcases = readInput('4_test.in')
    results = map(lambda testcase: solve(testcase), testcases)
    writeOutput(results, '4_test.out_tin')


if __name__ == "__main__":
    main()
