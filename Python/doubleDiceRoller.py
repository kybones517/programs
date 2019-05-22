import random as r
die = []
die2 = []
for i in range(1,7):
	die.append(i)
	die2.append(i)

rollnum = input("How many times you wanna roll?\n" )
double = 0
for i in range(int(rollnum)):
	rolldie1 = r.choice(die)
	rolldie2 = r.choice(die)
	totalRoll = rolldie1 + rolldie2
	print("You rolled:",totalRoll)
	print("[%s] + [%s]" % (rolldie1,rolldie2))
	if(rolldie1 == rolldie2):
		print("Double!")
		double+=1
print("Doubles:",double)
if double >=1:
	print(int(rollnum)/int(double),"%")
