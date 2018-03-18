import random

def write_testcase(results, filename='test9.in'):
    """
    write testcases
    :param filename: filename
    :return: write testcases to file
    """
    lines = map(lambda result: ' '.join(map(lambda x: str(x), result)), results)
    f = open(filename, 'w')
    f.write(str(len(results)) + '\n')
    f.write('\n'.join(lines))
    f.close()

n_tests = 100
testcases = []
for i in range(n_tests):
    l = int(random.gauss(i*i + 10, (i*i + 10)/10))
    collision_rate = random.randint(0, 80)/100.0
    a = map(lambda x: random.randint(0, int((1.0-collision_rate)*l)), range(l))
    testcases += [a]
write_testcase(testcases)