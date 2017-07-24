import random 
fh = open("hangdata.txt","r")
data_Read = fh.read()
sort_Data= data_Read.split(" ")
sort_d = []
for x in sort_Data:
	if x != "\n":
		sort_d.append(x)
countn = 0		
count_wrong = 0

for x in sort_d:
	countn = countn + 1


#print("Enter any number from 1 to 50")
a = random.randint(0,50)

decide_num = a % countn


choosen_word = sort_d[decide_num]

count_a = 0
for x in choosen_word:
	count_a = count_a + 1
	


choosen_a = a % count_a 

man_list = [
''' 			+-------+
			|	|
				|
				|
				|
				|
				|
				|
		================= ''',
 '''			+-------+
			|	|
			O	|
				|
				|
				|
				|
				|
		================= ''',
'''			+-------+
			|	|
			O	|
			|	|
				|
				|
				|
				|
		================= ''',
''' 			+-------+
			|	|
			O	|
			|	|
		       /	|
				|
				|
				|
		================= ''',
''' 			+-------+
			|	|
			O	|
			|	|
		       / \	|
				|
				|
				|
		================= ''',
'''		        +-------+
			|	|
			O	|
		       -|	|
		       / \	|
				|
				|
				|
		================= ''',
''' 			+-------+
			|	|
			O	|
		       -|-	|
		       / \	|
				|
		    HangMan	|
				|
		================= '''
]

choosen_wordL = list(choosen_word)
game_list = list(choosen_word)
i = 0

while count_a > i:
	game_list[i] = 0
	i = i + 1
j = 0 
e = 0
choosen_alp = choosen_wordL[choosen_a]
for x in  choosen_wordL:
	if x == choosen_alp:
		 game_list[e] = x
	e = e + 1	
counter = 0	
j = 0	
k = 0

for x in game_list:
	if x != 0:
		print x,
	else:
		print "_",

while count_wrong < 6:
	k = 0	
	
	print("Guess Word")
	c=raw_input()
	if c in choosen_wordL and c  not in game_list:
			print(man_list[count_wrong])
			print'\n'
			for x in choosen_wordL:
				if x == c:
					game_list[j] = c
				j = j + 1
				
			for x in game_list:
				if x != 0:
					print x,
				else:
					print "_",

			for x in game_list:
				
				if x != 0:
					k = k + 1
			if k == count_a:
				print("You win")
				break
					
	elif c in choosen_wordL or game_list:
			print("Guessed Wrong")
			count_wrong = count_wrong + 1
			print(man_list[count_wrong])
			for x in game_list:
				if x != 0:
					print x,
				else:
					print "_",
			
	j = 0
	
if(count_wrong >= 6):
	print("You Lost")			











