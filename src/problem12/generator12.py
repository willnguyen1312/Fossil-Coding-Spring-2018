import random

def write_testcase(results, filename='test12.in'):
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

n_tests = 300
testcases = []
for i in range(n_tests):
    l = int(random.gauss(pow(i, 1.2) + 10, (pow(i, 1.2) + 10)/10))
    def gen_num(avg_length):
        num_length = max(int(random.gauss(avg_length, avg_length)), 1)
        return ''.join(map(lambda x: str(random.randint(0,9)),range(num_length)))
    avg_length = random.randint(5, 20)
    a = map(lambda x: gen_num(avg_length), range(l))
    testcases += [a]
write_testcase(testcases)