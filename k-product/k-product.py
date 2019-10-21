"""
Design/implement a class that supports inserting integers and getting the 
product of K most recently inserted numbers (K is provided at the time of 
construction).

K = 3
[1, 3] => 3
[1, 3, 4] => 12
[1, 3, 4, 0] => 0
[1, 3, 4, 0, 6] => 0
[1, 3, 4, 0, 6, 1] => 0
[1, 3, 4, 0, 6, 1, 5] => 30
"""

from collections import deque


class KProduct:
    def __init__(self, k):
        self.k = k
        self.numZeros = 0
        self.product = 1
        self.queue = deque()

    def insert(self, num):
        self.queue.append(num)
        if num == 0:
            self.numZeros += 1
        else:
            self.product *= num

        if len(self.queue) > self.k:
            poppedNum = self.queue.popleft()
            if poppedNum == 0:
                self.numZeros -= 1
            else:
                self.product /= poppedNum

    def getProduct(self):
        if self.numZeros > 0:
            return 0
        return self.product


kProduct = KProduct(3)
kProduct.insert(1)
print(kProduct.getProduct())
kProduct.insert(3)
print(kProduct.getProduct())
kProduct.insert(4)
print(kProduct.getProduct())
kProduct.insert(0)
print(kProduct.getProduct())
kProduct.insert(6)
print(kProduct.getProduct())
kProduct.insert(1)
print(kProduct.getProduct())
kProduct.insert(5)
print(kProduct.getProduct())
