# def recursionMethod(param):
#     if "exit from cond. satisfied":
#         return something
#     else:
#         recursionMethod(modified_params)

def recursionMethod(n):
    if n<1:
        print("n less than 1")
    else:
        recursionMethod(n-1)
        print(n)

# recursionMethod(5)

def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2

# print(powerOfTwo(4))

def factorial(n):
    assert n >= 0 and int(n) == n, "Enter proper values for factorial"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(5))

def fibbonaci(n):
    assert n >= 0 and int(n) == n, "Enter proper values"
    if n in [0,1]:
        return n
    else:
        return fibbonaci(n-1) + fibbonaci(n-2)

def printFibonacciSeries(n):
    series = ''
    for i in range(0, n, 1):
        series = series + str(fibbonaci(n)) + ' ,'
        n = n - 1
    print((series + '0')[::-1])

# printFibonacciSeries(10)

def sumOfDigits(n):
    assert n >= 0 and int(n) == n, "Enter proper values"
    if n < 10:
        return n
    else:
        return int(n%10) + sumOfDigits(int(n/10))

# print(sumOfDigits(501))

def power(base, exp):
    assert exp >= 0 and int(exp) == exp, "Enter proper values"
    if exp == 0:
        return 1
    else:
        return base * power(base, exp-1)

# print(power(5, 2))

def gcd(a, b):
    assert int(a) == a and int(b) == b, 'Integers only, positive or negetive both allowed'
    #gcd of positive and negetive number are same, so converting negative int to postive if passed
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    #main logic
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

# print(gcd(48, -18))

def toBinary(n):
    assert int(n) == n, 'Only Integers are allowed!'
    if n == 0:
        return 0
    else:
        return (n%2) + (10 * toBinary(int(n/2)))

# print(toBinary(14))

def maxInArray(arr, n):
    if n == 1:
        return arr[0]
    else:
        return max(arr[n-1], maxInArray(arr, n-1))

# print(maxInArray([11,7,12,4,6,7], 6))

def reverse(strng):
    if len(strng) == 1:
        return strng
    else:
        return strng[-1:] + str(reverse(strng[:-1]))

# print(reverse('hello'))

# print("HELLO"[:1])
# print("HELLO"[-1:])
# print("HELLO"[:-1])
# print("HELLO"[1:])
# print("HELLO"[1:-1])

def isPalindrome(strng):
    if len(strng) in [0,1]:
        return True
    elif strng[:1] != strng[-1:]:
        return False
    else:
        return isPalindrome(strng[1:-1])

# print(isPalindrome('saras'))