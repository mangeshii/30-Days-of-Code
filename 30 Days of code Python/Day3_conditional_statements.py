'''
Task
Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20 , print Weird
If  is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.

Input Format:
A single line containing a positive integer .

Output Format:
Print Weird if the number is weird; otherwise, print Not Weird.

'''


if __name__ == '__main__':
    N = int(input())

    if N % 2 != 0:
        print('Weird')
    elif N % 2 == 0 and (N >= 2 and N < 5):
        print('Not Weird')
    elif N % 2 == 0 and (N >= 6 and N <= 20):
        print('Weird')
    elif N % 2 == 0 and (N > 20):
        print('Not Weird')
