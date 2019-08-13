def getSeat(seat_no):
	nP6 = seat_no % 6
	n6P2 = (seat_no / 6) % 2
	frontSeat = ""
	difference = 0
	if(nP6 == 0 or nP6 == 1):
		if(n6P2 == 0):
			difference = 11
		else:
			difference = 1
		if(nP6 == n6P2):
			frontSeat = seat_no - difference
		else:
			frontSeat = seat_no + difference
		return (str(frontSeat) + " WS")
	elif(nP6 == 5 or nP6 == 2):
		if(nP6 == 5 and n6P2 == 0):
			frontSeat = seat_no + 3
		elif(nP6 == 2 and n6P2 == 0):
			frontSeat = seat_no + 9
		elif(nP6 == 5 and n6P2 == 1):
			frontSeat = seat_no - 9
		elif(nP6 == 2 and n6P2 == 1):
			frontSeat = seat_no - 3
		return (str(frontSeat) + " MS")
	elif(nP6 == 3 or nP6 == 4):
		if(nP6 == 3 and n6P2 == 0):
			frontSeat = seat_no + 7
		elif(nP6 == 4 and n6P2 == 0):
			frontSeat = seat_no + 5
		elif(nP6 == 3 and n6P2 == 1):
			frontSeat = seat_no - 5
		elif(nP6 == 4 and n6P2 == 1):
			frontSeat = seat_no - 7
		return (str(frontSeat) + " AS")

T = input()
nums = list()
results = list()
for i in range(int(T)):
    nums.append(int(input()))
    results.append(getSeat(nums[i]))

for i in results:
    print(i)