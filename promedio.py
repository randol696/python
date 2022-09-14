
counter = 0

while counter < 3:
    print("-------------------------")
    print("Average Grade Calculator")
    n1 = float(input("Base :"))
    n2 = float(input("Nota :"))
    promedio = (n2/n1)*4+1
    print ("resultado :" + str (promedio))

    counter = counter + 1
else:
    print("OUT")