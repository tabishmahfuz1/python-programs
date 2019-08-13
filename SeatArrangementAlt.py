str = ""
for i in range(1, 108, 6):
	str = str + "WMAAMW"
	
def getFrontSeat(seat_no):
	compartment_pos = seat_no % 12;
	return (13 - compartment_pos)