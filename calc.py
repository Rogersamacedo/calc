def calculadora():
    print("Qual operação deseja efetuar? : ")
    print( "Para soma digite 1")
    print( "Para subtração digite 2")
    print( "Para divisão digite 3")
    print( "Para mutiplicação digite 4")
    print( "Para potencia digite 5")
    print( "Para porcentagem digite 6")
    print( "Para raiz quadrada digite 7")
    #operacao = 7
    #num = float(input("Inofrme o numero que vc quer saber a raiz quadrada: "))
    #print(float(num) ** 0.5)
    operacao = int(input("Digite a sua opção: "))
    
    while operacao < 1 or operacao > 7:
    
        print("DIGITE A OPÇÃO ENTRE 1 E 7")
        break;
            
    num1 = float(input("Informe o primeiro numero: "))
    num2 = float(input("Informe o segundo numero: "))
    
    if operacao == 1 :
        print(num1 + num2)
    elif operacao == 2 :
        print(num1 - num2)
    elif operacao == 3 :
        print(num1 / num2)
    elif operacao == 4 :
        print(num1 * num2)
    elif operacao == 5 :
        print(num1 ** num2)
    elif operacao == 6 :
        p = (num1/100)
        print(p, "%",  "de", num2, "é", (num1/100) * num2)
    elif operacao == 7:
        num = float(input("Inofrme o numero que vc quer saber a raiz quadrada: "))
        print(float(num) ** 0.5)
calculadora()

