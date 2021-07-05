#! /usr/bin/env python

'''
#1부터 10까지 다 더하는 방법

val = 0

for i in range(1, 11):
    val += i

print(val)

# 2의 배수 구구단만 출력하기

for i in range(2,10):
    if i % 2 == 0:
        for j in range(1, 10):
            print('{}*{} = '.format(i,j),i*j)

# 5! 계산하는 방법

import sys

n = int(sys.argv[1])
val = 1

while n>0:
    val *= n
    n -= 1
print(val)

'''

def greet():
    print('Hello, Bioinformatics')
def greet1(name):
    print(f'Hello,{name}')


greet()
greet1("ken")
