weight = input('Enter your weight in kg: ')
height = input('Enter your height in m: ')

bmi = int(weight) / float(height) ** 2
print(bmi)
print(round(bmi, 2))

print(bmi / 2)
print(round(bmi / 2))

new_bmi = bmi // 2
print(new_bmi)