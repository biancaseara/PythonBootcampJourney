# Functions with Outputs
def format_name(f_name, l_name):
    '''
    Take a first name and last name, then returns formated in title case. 
    '''
    f_name = f_name.title()
    l_name = l_name.title()

    return f"{f_name} {l_name}"

first_name = 'BIANCA' #input('Type your first name: ')
last_name = 'seara' #input('Type your last name: ')

print(format_name(f_name=first_name, l_name=last_name))

# if operation_symbol == '+':
#     answer = add(num1, num2)
# elif operation_symbol == '-':
#     answer = subtract(num1, num2)
# elif operation_symbol == '*':
#     answer = multiply(num1, num2)
# elif operation_symbol == '/':
#     answer = divide(num1, num2)