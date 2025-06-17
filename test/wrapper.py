from loggerpython import Logger


@Logger
def add(a, b):
    return a+b


# Irrespective of the placement of set_loglevel, the level is applied over the program from start.
Logger.set_loglevel("DEBUG")


@Logger
def multiply(a, b):
    result = a * b
    if result < 0:
        Logger.critical(f"Result is {result} which is less than 0")
    return result


print(add(10, 20))
print(multiply(20, -30))
