
def sieve(num):
    if num < 2:
        raise Exception('invalid input')
    numbers = []
    # create list
    for i in range(num+1):
        numbers.append(True)
    numbers[0] = False
    numbers[1] = False
    # sieve list
    for i in range(2, num+1):
        for j in range(i+i, num+1, i):
            numbers[j] = False
    # display list
    for i in range(num+1):
        if numbers[i]:
            print(i)

if __name__ == '__main__':
    sieve(30)
