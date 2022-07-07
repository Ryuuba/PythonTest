while True:
    try:
        input_str = input('Enter a natural number: ')
        value = int(input_str)
        if value < 0:
            raise ValueError
        reciprocal = 1/value
    except KeyboardInterrupt:
        print('Program ends manually')
        break
    except ValueError:
        print('Input {} cannot be processed'.format(input_str))
    except ZeroDivisionError:
        print('Division by zero is not allowed in our Universe.')
    except:
        print('Unknown error')
    else:
        print('The reciprocal of', value, 'is', reciprocal)        
        break
