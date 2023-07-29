def div(x, y):
    try:
        result = x/y
        print(result)
    except ValueError as ve:
        print(ve + ": " + "please check your value")
    except TypeError as te:
        raise TypeError("Value")
        print(te + ": " + "please write just number")
    except ZeroDivisionError:
        ZeroDivisionError("please dont divide by zero")
        raise ZeroDivisionError("please dont divide by zero")
    else:
        print("else")
    finally:
        print("finally")


div(5, 0)
a = 5
c = 0

try:
    quotient = a / c
    print(quotient)
except (ZeroDivisionError, TypeError):
    print("You cannot divide by zero and variables must be floats or integers")
except:
    print("Other error")


