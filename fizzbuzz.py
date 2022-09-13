
def fizz(input):
    return 'Fizz' if input % 3 == 0 else ''

def buzz(input):
    return 'Buzz' if input % 5 == 0 else ''

def main(end, checks):
    for i in range(1, end+1):
        output = ''
        for check in checks:
            output += check(i)
        if output == '':
            print(i)
        else:
            print(output)

if __name__ == '__main__':
    main(20, [fizz,buzz])
