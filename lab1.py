import math as m
import op1 as op1
import op2 as op2
import op3 as op3
#HOLA QUE HACE

op=99
opa=0
can=0
acumu=0.0
res=0
print("Bienvenido a la calculadora")
print("quiere que sea acumulativo? (1=si, 0=no)")
opa=int(input())

while op!=0 :

    print("Seleccione la operacion que desea realizar")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Maximo Comun Divisor")
    print("6. Minimo Comun Multiplo")
    print("7. Seno")
    print("8. Coseno")
    print("9. Tangente")
    print("10. Factorial")
    print("11. Fibonacci")
    print("12. Raiz enesima")
    print("13. Potencia")
    print("14. IVA")
    op=int(input())
    match op:
        case 1:
            if opa==0 or can==0:
                print("Ingrese el numero que se va a sumar")
                num1=int(input())
                can+=1
            else:
                num1=acumu
            print("Ingrese el segundo numero a sumar")
            num2=int(input())
            res=op1.op1(num1,num2,res)
            if opa==1:
                acumu=float(res.suma()  )
            else:
                print("El resultado es: ",res.suma())


        case 2:
            if opa==0 or can==0:
                    print("Ingrese el primer numero a restar")
                    num1=int(input())
                    can+=1
            else:
                    num1=acumu
            print("Ingrese el segundo numero a restar")
            num2=int(input())
            res=op1.op1(num1,num2,res)
            if opa==1:
                acumu=res.rest()
            else:
                print("El resultado es: ",res.rest())
        case 3:
            if opa==0 or can==0:
                print("Ingrese el primer numero a multiplicar")
                num1=int(input())
                can+=1
            else:
                num1=acumu
            print("Ingrese el otro numero a multiplicar")
            num2=int(input())
            res=op1.op1(num1,num2,res)
            if opa==1:
                acumu=float(res.multi() )
            else:
                print("El resultado es: ",res.multi())
        case 4:
            if opa==0 or can==0:
                print("Ingrese el primer numero a dividir")
                num1=int(input())
                can+=1
            else:
                num1=acumu
            print("Ingrese el segundo numero a dividir")
            num2=int(input())
            if num2==0:
                print("No se puede dividir entre cero")
            else:
                res=op1.op1(num1,num2,res)
                if opa==1:
                    acumu=res.divi()
                else:
                    print("El resultado es: ",res.divi())
        case 5:
            if opa==0 or can==0:
                print("Ingrese el primer numero a calcular el MCD")
                num1=int(input())
                can+=1
            else:
                num1=acumu
            print("Ingrese el otro numero a calcular el MCD")   
            num2=int(input())
            res=op1.op1(num1,num2,res)
            if opa==1:
                acumu=res.mcd()
            else:
                print("El resultado es: ",res.mcd())
        case 6:
            if opa==0 or can==0:
                print("Ingrese el primer numero a calcular el MCM")
                num1=int(input())
                can+=1
            else:
                num1=acumu
            print("Ingrese el otro numero a calcular el MCM")
            num2=int(input())
            res=op1.op1(num1,num2,res)
            if opa==1:
                acumu=res.mcm()
            else:
                print("El resultado es: ",res.mcm())
        case 7:
            if opa==0 or can==0:
                print("Ingrese el numero para calcular el seno")
                num1=int(input())
                can+=1
            else:
                num1=acumu
            res=op2.op2(num1,res)
            if opa==1:
                acumu=res.sen()
            else:
                print("El resultado es: ",res.sen())
        case 8:
            if opa==0 or can==0:
                print("Ingrese el numero para calcular el coseno")
                num1=int(input())
                can+=1
            else:
                num1=acumu
            res=op2.op2(num1,res)
            if opa==1:
                acumu=res.cos()
            else:
                print("El resultado es: ",res.cos())
        case 9:
            if opa==0 or can==0:
                print("Ingrese el numero para calcular la tangente")
                num1=int(input())
                can+=1
            else:
                num1=acumu
            res=op2.op2(num1,res)
            if opa==1:
                acumu=res.tan()
            else:
                print("El resultado es: ",res.tan())
        case 10:
            if opa==0 or can==0:
                print("Ingrese el numero para calcular el factorial")
                num1=int(input())
                can+=1
            else:
                num1=acumu
            res=op2.op2(num1,res)
            if opa==1:
                acumu=res.fact()
            else:
                print("El resultado es: ",res.fact())
        case 11:
            if opa==0 or can==0:
                print("Ingrese el numero para calcular la serie de Fibonacci")
                num1=int(input())
                can+=1
            else:
                num1=acumu
            res=op2.op2(num1,res)
            if opa==1:
                acumu=res.fibonachi()
            else:
                print("El resultado es: ",res.fibonachi())
        case 12:
            if opa==0 or can==0:
                print("Ingrese el primer numero para calcular la raiz enesima")
                num1=int(input())
                can+=1
            else:
                num1=acumu
            if num1<0:
                print("No se puede calcular la raiz de un numero negativo")
            else:
                print("Ingrese el indice de la raiz")

                num2=int(input())
                res=op3.op3(num1,num2,res)
                res.raiz()
                print("El resultado es: ",res.raiz())
        case 13:
            if opa==0 or can==0:
                print("Ingrese el primer numero para calcular la potencia")
                num1=int(input())
                can+=1
            else:
                num1=acumu
            print("Ingrese el exponente de la potencia")
            num2=int(input())
            res=op3.op3(num1,num2,res)
            res.poten()
            print("El resultado es: ",res.poten())
        case 14:
            if opa==0 or can==0:
                print("Ingrese el primer numero para calcular el IVA")
                num1=int(input())
                can+=1
            else:
                num1=acumu
            print("Ingrese el segundo numero")
            num2=int(input())
            res=op3.op3(num1,num2,res)
            res.iva()
            print("El resultado es: ",res.iva())

    
    if opa==1:
        print("El resultado acumulado es: ",acumu)  
        print("Quieres que se reinicie el acumulado? (1=si, 0=no)")
        op=int(input())
        if op==1:
            acumu=0

    
    print("Desea realizar otra operacion? (1=si, 0=no)")
    op=int(input())
    if op==0:
            print("Gracias por usar la calculadora")
