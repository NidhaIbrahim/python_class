# a = 10
# b = 0
# result = 0

# result = a / b
# print(result)

# print('hello')


a = 10
b = 0
result = 0

try:
    result = a / b
except ZeroDivisionError as e:
    print(e)

print('hello')

file = ""
try:
    file = open('./demofile.txt', 'r')
    print(file.read())
    # file.write('This is a test file')
    # file.close()
except FileNotFoundError:
    print("Error: Can't find file or read data")
else:
    print("Written content in the file successfully")
finally:
    print('Program execution successfully')
