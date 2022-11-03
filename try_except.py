a = 14
b = 0

try:
    f = open('file3.txt')
    content = f.read()
    print(content)
    print(a/b)

except ZeroDivisionError as z:
    print(z)

except FileNotFoundError as err:
    print(err)

except Exception as e:
    print(e)

finally:
    print("Important")
    # f.close()