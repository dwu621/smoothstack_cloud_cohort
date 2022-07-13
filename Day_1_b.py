# 1
num1 = 50 + 50
num2 = 100 - 10
print(num1 + num2)
# output 190

# 2
# print(30+*6)
# output syntax error

print(6 ^ 6)
# output 0

print(6 ** 6)
# output 46656

print(6 + 6 + 6 + 6 + 6 + 6)
# output 36

# 3
print("Hello World")
# output Hello World

print('“Hello World : 10”')
# output “Hello World : 10”

# 4


def calc_monthly(p, r, l):
    m = round((p * (r * .01 / 12) * ((1 + r * .01 / 12) ** l)) /
              (((1 + r * .01 / 12) ** l) - 1))
    return m


print(calc_monthly(800000, 6, 103))
# output 9957
