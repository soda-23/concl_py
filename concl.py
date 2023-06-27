print('Добро пожаловать!')
while True:
    
    try:
        
        num1 = int(input('Введите первое число: '))
        oper = input('Введите  операцыю >> ')
        num2 = int(input('Введите второе число: '))
        
        if oper == '+':
            print(num1 + num2)
        elif oper == '-':
            print(num1 - num2)
        elif oper == '/':
            print(num1 / num2)
        elif oper == '*':
            print(num1 * num2)
    except ValueError:
        print('Вы не вели число!')
    except ZeroDivisionError:
        print('На ноль не делится')
    else:
        oper2 = str(input('Вы хотите продолжет нет|да: '))
        if oper2 == 'нет':
            break
        if oper2 == 'next':
            break
        else:
            print('продолжим наш проект')

       
       re
       
       
       
       
       

           




