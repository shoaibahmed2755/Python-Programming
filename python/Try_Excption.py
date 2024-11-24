def spam(num): 
    try:
        return 42/num
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"
print(spam(0))