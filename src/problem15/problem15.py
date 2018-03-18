

def readInput(filename='test15.in'):
    """
    read input file
    :param filename: filename
    :return: an array of testcases, each testcase is an array of numbers
    """
    f = open(filename, 'r')
    f.readline()
    lines = map(lambda x: map(lambda y: int(y), x.strip().split(' ')), f.readlines())
    return lines


def solve(a):
    """
    solve the problem: given a number, keep sum the
    :param a: an array of input numbers
    :return: output array that has been removed duplicated numbers
    """
    x1 = a[0]
    y1 = a[1]
    x2 = a[2]
    y2 = a[3]
    x3 = a[4]
    y3 = a[5]
    x4 = a[6]
    y4 = a[7]

    def parallel((dx1, dy1), (dx2, dy2)):
        return dx1 * dy2 == dx2 * dy1

    def delta(x1, y1, x2, y2):
        return (x2-x1, y2-y1)

    d1 = delta(x1, y1, x2, y2)
    d2 = delta(x3, y3, x4, y4)
    d3 = delta(x1, y1, x3, y3)
    return parallel(d1, d2) and not parallel(d1, d3)


def writeOutput(results, filename='test15.out'):
    """
    write output file
    :param filename: filename
    :return: write results to file
    """
    lines = map(lambda x: "YES" if x else "NO" ,results)
    f = open(filename, 'w')
    f.write('\n'.join(lines))
    f.close()


def main():
    testcases = readInput()
    results = map(lambda testcase: solve(testcase), testcases)
    writeOutput(results)


if __name__=='__main__':
    main()