# 05.07
# Task 1
p = 0
n = 0
list1 = [1, 2, 3, 4, 5, 6, -6, -5, -4, -3, -2, -1, 132, 456, 0, 0, 1, 4, 4, -6, 2, 6, -7]
for i in list1:
    if i >= 0:
        p+=1
    if i < 0:
        n+=1
print(f"Positive count: {p}, Negative count: {n}")
# Task 2
list2 = [1, 2, 3, 4, 5, 6, -6, -5, -4, -3, -2, -1, 132, 456, 0, 0, 1, 4, 4, -6, 2, 6, -7]
for index, i in enumerate(list2):
    if i < 0:
        break
    else:
        continue
print(f"First negative element is {i} its Index {index}")

# Task 3
list3 = [-6, -5, -4, -3, -2, -1, 132, 456, 0, 0, 1, 4, 4, -6, 2, 6, -7]
for index, i in enumerate(list3):
    if i > 0:
            break
    else:
        continue
print(f"First positive element is {i} its Index {index}")

# Task 4
list4 = [0, 0, 1, 4, 4, -6, -2, -6, 7]
ln = None
li = -1
for index, i in enumerate(list4):
    if i < 0:
        ln= i
        li = index
    else:
        continue
print(f"Last negative element: {ln}, Index: {li}")
# 08.07
#Task1
def m_t(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
num = int(input("Введіть число для друку таблиці множення: "))
m_t(num)
#Task2
def s_l(s):
    return len(s)
i_s = input("Введіть рядок: ")
print(f"Довжина рядка: {s_l(i_s)}")
#Task3
def change_case(s):
    return s.swapcase()
i_st = input("Введіть рядок: ")
print(f"Рядок зі зміненим регістром: {change_case(i_st)}")
#Taks4
def n_t(a, b, c):
    return (a + b + c) / 3
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))
print(f"Середнє значення: {n_t(num1, num2, num3)}")
#Task5
def m_t(a, b, c):
    return max(a, b, c)
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))
print(f"Максимальне число: {m_t(num1, num2, num3)}")