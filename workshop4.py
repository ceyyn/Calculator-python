plus = lambda num1, num2 : num1 + num2
extraction = lambda num1, num2 : num1 - num2
division = lambda num1, num2 : num1 / num2
multiplication = lambda num1, num2 : num1 * num2
fact = 1
while True:
    x = input("\n 1: Topla \n 2: Çıkar \n 3: Böl \n 4: Çarp \n 5: Faktoriyel \n Enter the operation : ")
    num1 = int(input("Enter a value : "))
    if x == "5":
        if num1 < 0 :
            print("Hatalı değer girildi.")
        for i in range(1,num1+1):
            fact = fact * i
        print("\nResult : " + str(fact))
    if not x == "5":
        num2 = int(input("Enter the second value :  "))
        if x == "1":
            print("\nResult : " + str(plus(num1, num2)))
        elif x == "2":
            print("\nResult : " + str(extraction(num1, num2)))
        elif x == "3":
            print("\nResult : " + str(division(num1, num2)))
        elif x == "4":
            print("\nResult : " + str(multiplication(num1, num2)))
        else :
            print("\nOperation is cannot defined. Please try again.")