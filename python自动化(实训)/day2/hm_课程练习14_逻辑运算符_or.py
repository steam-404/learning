"""
需求：
提示用户输入一个数字，判断它是否能被3或者5整除
"""
numbers = int(input("please enter numbers"))

if numbers % 3 == 0 or numbers % 5 == 0:
    print("可以")
else:
    print("不可以")
