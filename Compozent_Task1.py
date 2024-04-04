class calculator:
    def add(self, n1, n2):
        return n1 + n2
    def sub(self, n1, n2):
        return n1 - n2
    def mul(self, n1, n2):
        return n1 * n2
    def div(self, n1, n2):
        return n1 % n2

while True:
    n1 = float(input("Enter the First NUmber= "))
    s = input("Enter the operator= ")
    n2 = float(input("Enter the Second NUmber= "))

    operation = calculator()

    if s == '+':
        print(operation.add(n1, n2))
    elif s == '-':
        print(operation.sub(n1, n2))
    elif s == '*':
        print(operation.mul(n1, n2))
    elif s == '/':
        print(operation.div(n1, n2))
    else:
        print("Invalid Input")

    again = input("Enter yes to continue= ")
    if again == "yes":
        continue
    else:
        break