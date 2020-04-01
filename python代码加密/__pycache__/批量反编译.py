# encoding=utf8
import os
import uncompyle6
from uncompyle6 import decompile_file
def main():
    path = 'C:\filename'.decode('utf8')        # Windows下
    for root, dirs, files in os.walk(path):
        if root != path:
            break
        for filename in files:
            if filename.endswith('pyc'):
                print filename
                os.system('uncompyle6 -o . %s'%filename)
    
if __name__ == '__main__':
    main()