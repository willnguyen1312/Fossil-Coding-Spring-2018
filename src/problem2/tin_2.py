# -*- coding: utf-8 -*-
import codecs


def readInput(filename='test2.in'):
    """
    read input file
    :param filename: filename
    :return: an array of testcases, each testcase is an array of numbers
    """
    f = codecs.open(filename, encoding='utf-8', mode='r')
    lines = map(lambda x: x.strip('\n'), f.readlines())
    return lines


def solve(a):
    """
    solve the problem
    :param a: an array of input numbers
    :return: output array that has been removed duplicated numbers
    """
    s = u""
    while len(a) > 0:
        map_3 = {
            u"ngh": u"q",
        }
        map_2 = {
            u"ng": u"q",
            u"tr": u"c",
            u"ch": u"c",
            u"nh": u"n'",
            u"th": u"w",
            u"kh": u"x",
            u"gh": u"g",
            u"ph": u"f",
        }
        map_1 = {
            u"q": u"k",
            u"c": u"k",
            u"r": u"z",
            u"d": u"z",
            u"đ": u"d",
        }
        if a[:3] in map_3:
            s += map_3[a[:3]]
            a = a[3:]
            continue
        if a[:2] in map_2:
            s += map_2[a[:2]]
            a = a[2:]
            continue
        if a[0] in map_1:
            s += map_1[a[0]]
            a = a[1:]
            continue
        s += a[0]
        a = a[1:]

    return s


def writeOutput(results, filename='test2.out'):
    """
    write output file
    :param filename: filename
    :return: write results to file
    """
    lines = results
    f = codecs.open(filename, encoding='utf-8', mode='w')
    f.write('\n'.join(lines))
    f.close()


def main():
    testcases = readInput('2.in')
    results = map(lambda testcase: solve(testcase), testcases)
    writeOutput(results,'2.out_tin')


if __name__ == "__main__":
    main()
