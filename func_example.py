# An example of functions in Python

ages = [10, 20, 30, 40]
incomes = [100, 200, 300, 400]

# parameters passed into the function are between the brackets.
def calculateAverage(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum/len(list)

# Parameter passed into the function below
print(calculateAverage(incomes))