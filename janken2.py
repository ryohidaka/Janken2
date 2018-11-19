import random
import collections

random.seed()

hand = [0, 1, 2]
aiko = 0
block = 0 #0
paper = 0 #1
scissors = 0 #2
people = [0,0,0]

print('Person')
person = int(input())
print('Count')
many = int(input())
print('\n')

for i in range(0, many):
	player = random.choices(hand, k = person)
	print('手:{}'.format(player))
	
	result = collections.Counter(player)
	result = len(result)
	print('要素数: {} 個'.format(result))
	
	if result == 2:
		if player.count(2) == 0: #グーとチョキ
			block = block + 1
			blockperson = player.count(0)
			people[0] = people[0] + blockperson
			print('勝ち:グー {}人\n'.format(blockperson))
			
		elif player.count(1) == 0: #パーとグー
			paper = paper + 1
			paperperson = player.count(2)
			people[2] = people[2] + paperperson
			print('勝ち:パー {}人\n'.format(paperperson))
			
		elif player.count(0) == 0: #チョキとパー
			scissors = scissors + 1
			scissorsperson = player.count(1)
			people[1] = people[1] + scissorsperson
			print('勝ち:チョキ {}人\n'.format(scissorsperson))
			
		else :
			print('error2')
	elif result == 3:
		aiko = aiko + 1
		print('あいこ\n')
	elif result == 1:
		aiko = aiko + 1
		print('あいこ\n')
	else:
		print('error3')
		
print('{}人'.format(person))
print('グー: {} 回'.format(block))
print('チョキ: {} 回'.format(scissors))
print('パー: {} 回'.format(paper))
print('あいこ: {} 回\n'.format(aiko))
