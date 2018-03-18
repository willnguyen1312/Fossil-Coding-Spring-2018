import random
import datetime

def write_testcase(results, filename='test10.in'):
    """
    write testcases
    :param filename: filename
    :return: write testcases to file
    """
    lines = results
    f = open(filename, 'w')
    f.write(str(len(results)) + '\n')
    f.write('\n'.join(lines))
    f.close()

n_tests = 1000
testcases = []
for i in range(n_tests):
    d = datetime.date(1,1,1) + datetime.timedelta(random.randint(0, 365*8000))
    testcases += ["%02d/%02d/%04d" %(d.day, d.month, d.year)]
write_testcase(testcases)