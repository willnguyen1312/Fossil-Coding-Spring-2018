import random

def write_testcase(results, filename='test11.in'):
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
    avg_pts = random.randint(500, 1500)
    pts = map(lambda x: int(random.gauss(avg_pts, avg_pts/10)), range(l))
    goals = map(lambda x: random.randint(0, 1000), range(l))
    testcases += [pts, goals]
write_testcase(testcases)