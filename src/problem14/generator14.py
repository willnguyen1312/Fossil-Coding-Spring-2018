import random

def write_testcase(results, filename='test14.in'):
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
    testcases += [''.join(map(lambda x: str(random.randint(0,9)),range(i+1)))]
write_testcase(testcases)