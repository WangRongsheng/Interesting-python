import re
def check(mystr):
    a = re.compile(r'[0-9a-zA-Z]{6,20}')
    if a.fullmatch(mystr) is None:
        return '密码只能包含英文字母和数字，长度6~20'
    return '密码安全'

def main():
    n = str(input("测试密码:"))
    print(check(n))

main()
