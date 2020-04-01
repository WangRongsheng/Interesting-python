# uncompyle6 version 3.5.0
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.1 (default, Dec 10 2018, 22:54:23) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: demo.py
# Size of source mod 2**32: 208 bytes
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != k:
                if i != j:
                    if j != k:
                        print(i, j, k)