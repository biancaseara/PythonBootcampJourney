songs = ['twenty', '_world', 'kidult', 'boomboom', 'mansae']

for song in songs:
    print(song)
    print('I really like: ' + song)

# For loop with range(start, end, step)
# for number in range(1, 11, 3):
#     print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)

sum_num = 0
for number in range(1, 101):
    if (number % 2 == 0):
        sum_num += number
print(sum_num)

total_even_num = 0
for number in range(2, 101, 2):
    total_even_num += number
print(total_even_num)