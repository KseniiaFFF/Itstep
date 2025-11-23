def input_calc(x, znak, y):

    while True:
        try:
            x = int(x)
            y = int(y)
            if x == 00:
                print('Exit')
                exit()

            if znak == '-':
             return x - y
            elif znak == '+':
             return x + y  
            elif znak == '*':
             return x * y  
            elif znak == '/':
             return x / y
            elif znak == '**':
             return x ** y
            else:
             return 'Error'  
        except ValueError:
            return 'no number'
        except TypeError:
           return 'unknow znak'
        except ZeroDivisionError:
            return 'del 0'
        finally:
            print('ok')

