# 學習函數功能

def wash():
    print("加水")
    print("加洗衣精")
    print("旋轉")

wash()
print("___________")

def wash2(dry):
    print("加水")
    print("加洗衣精")
    print("旋轉")
    if dry:
        print("烘乾")

wash2(dry = True)
print("___________")
wash2(True)
print("___________")

def add(x, y):
    print(x + y + 3)

add(40, 100)
add(50, 200)
add(10, y = 300)

def add2(x = 10, y = 100):
    print(x + y + 3)

add2(30, 500)
add2(50)
add2(30, y = 300)