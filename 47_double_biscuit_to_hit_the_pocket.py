#!/usr/bin/python3

# This problem is http://yukicoder.me/problems/89

first_line = input()
biscuits = int(first_line)

count = 0
while True:
    if biscuits <= 1 << count:
        break
    count += 1

print(count)
