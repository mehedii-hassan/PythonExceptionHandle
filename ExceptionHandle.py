try:
    list = [10, 0, 20]
    result = list[0] / list[3]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing by zero is not possible")
except IndexError:
    print("Invalid index")
finally:
    print("Successfull")