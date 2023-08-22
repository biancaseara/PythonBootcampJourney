print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

# name1 = name1.lower()
# name2 = name2.lower()

t = name1.count('t') + name2.count('t')
r = name1.count('r') + name2.count('r')
u = name1.count('u') + name2.count('u')
e = name1.count('e') + name2.count('e')
true_word = t + r + u + e

l = name1.count('l') + name2.count('l')
o = name1.count('o') + name2.count('o')
v = name1.count('v') + name2.count('v')
love_word = l + o + v + e

true_str = str(true_word)
love_str = str(love_word)

score_str = true_str + love_str
love_score = int(score_str)

if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos.') 
elif love_score >= 40 and love_score <= 50:
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')