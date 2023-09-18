# file = open('demo.txt', 'r')
# file.write('This is a test file')
# file.close()

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
