#!/bin/python3

import os
import sys

def aOrB(k, a, b, c):
    no = 0
    l = str(bin((a|b)^c))
    for i in l:
        if i is "1":
            no += 1
    if no > k:
        print(-1)
    else:
        # m = a & (~((a|b)^c))
        # n = ((~((a|b)^c)) & b) + (((a|b)^c) & c)
        x = bin((a|b)^c)[2:]
        y = list(bin(a)[2:])
        while len(y) != (len(hex(a))-2)*4:
            y.insert(0,'0')
        z = list(bin(b)[2:])
        while len(z) != (len(hex(b))-2)*4:
            z.insert(0,'0')
        for i, j in enumerate(x):
            if j == '1':
                if y[i] == z[i] and y[i] == '1':
                    y[i] = '0'
                    z[i] = '0'
                elif y[i] == z[i] and y[i] == '0':
                    y[i] = '1'
                    z[i] = '1'
                elif y[i] == '0' and z[i] == '1':
                    z[i] = '0'
                elif y[i] == '1' and z[i] == '0':
                    y[i] = '0'
            else:
                if y[i] == '1' and z[i] == '0':
                    y[i] = '0'
                    z[i] = 1 
        n = ''
        m = ''
        m = int(m.join(y), 2)
        n = int(n.join(z), 2)
        print(hex(m)[2:].upper())
        print(hex(n)[2:].upper())

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        k = int(input())
        a = int(input(),16)
        b = int(input(),16)
        c = int(input(),16)
        aOrB(k, a, b, c)