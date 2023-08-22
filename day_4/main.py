import random
'''
groups95 = ['JEONGHAN', 'SEUNGCHEOL', 'JISOO', 'JIMIN', 'TAEHYUNG']

groups95.append('JOSHUA')

groups95.extend(['NAYEON', 'WHEEIN', 'WOOZI'])

print(groups95)

groups95.remove('WOOZI')

groups95.reverse()

groups95.append('SEUNGCHEOL')
print(groups95)

print(groups95.count('SEUNGCHEOL'))
'''

seventeen = ['S.COUPS', 'JEONGHAN', 'JOSHUA', 'WOOZI', 'HOSHI', 'WONWOO', 'JUN', 'THE8', 'MINGYU', 'DK', 'VERNON', 'SEUNGKWAN', 'DINO']

print(seventeen[-5])

seventeen_len = len(seventeen)
random_num = random.randint(0, seventeen_len - 1)

print(f'{random_num + 1}: {seventeen[random_num]} || the random number was {random_num}')

seung_gi = ['vagabond', 'mouse']
seo_joon = ["what's wrong with the secretary Kim?", 'fighting for my way']
jong_suk = ['romance is a bonus book', 'w']

fav_actors_drama = [seung_gi, seo_joon, jong_suk]

print(f'{seung_gi}\n{seo_joon}\n{jong_suk}')

# row | column
print(fav_actors_drama[2][1])