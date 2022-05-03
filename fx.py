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


# 參數怎麼用
def wash2(dry, water):
    print("加水", water, "分滿")
    print("加洗衣精")
    print("旋轉")
    if dry:
        print("烘乾")

wash2(dry = True, water = 8)
print("___________")
wash2(True, 7)
print("___________")

def add(x, y):
    print(x + y + 3)

add(40, 100)
add(50, 200)
add(10, y = 300)

def add2(x = 10, y = 100):
    print(x + y + 3)

add2(30, 500)
add2(x = 50)
add2(30, y = 300)
print("_________")

# 學習return及學習儲存功能
def add3(x, y):
    return x + y + 3

result = add3(70, 500)
print(result)
print("_________")

# 變數可以是清單
# 要return你才會擁有這個值
def average(numbers):
    return sum(numbers) / len(numbers)

a = average([3, 60, 900])
print(a)
print("_________")

# 這樣也可以得到平均值但無法儲存
def average(numbers):
    print(sum(numbers) / len(numbers))

average([9, 30, 1200])