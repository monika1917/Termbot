# Calculator

def calc():
    print("Welcome to calculator!")
    first = float(input("First Number: "))
    second = float(input("Second Number: "))
    oper = input("Enter an operator (sum, diff, prod, quo, exp, mod) ")
    if(oper == "sum"):      # add
        answer = first + second
        print(answer)
    if(oper == "diff"):     # subtract
        answer = first - second
        print(answer)
    if(oper == "prod"):     # multiply
        answer = first * second
        print(answer)
    if(oper == "quo"):      # divide
        if second == 0:
            print("no")
        else:
            answer = first / second
            print(answer)
    if(oper == "exp"):      # exponent
        answer = first ** second
        print(answer)
    if(oper == "mod"):      # modulo
        answer = first % second
        print(answer)
