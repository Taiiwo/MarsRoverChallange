debug = False #turn debugging on and off
def locatechar(char,string): #prints the first location of a character in a string.
  if char in string:
		loop4 = -1
		stop = 0
		while stop == 0:
			loop4 = loop4 + 1
			if string[loop4] == char:
				result = loop4
				stop = 1
	else:
		result = False
	return result
#data gathering and validation
print "Please insert the coodinates of the top right most box."#This currently is used for nothing as I wasn't sure how it could be used.
print "Space separated, eg: '5 5'"
error = 1
while error == 1:#This 'error' system is here to create a loop that is broken only by error = 0 at the end.
	error = 0
	boxsize = raw_input("Coordinates:")
	if " " in boxsize:
		loc = locatechar(" ",boxsize)#see line 1 for locatechar()
		num1 = boxsize[:loc]
		num2 = boxsize[loc:]
	else:
		error = 1
	try:
		int(num1) + int(num2)
	except:
		error = 1
	if error == 1:
		print "Input invalid. Please read the instructions and try again."
loop = 1
rovers = []#createing rover location db
rovers.append(0)
compass = ('N','E','S','W')#This is used to convert 0, 1, 2, and 3 into directions and visa versa.
while loop == 1:
	print "Now input the current coordinates of the rover, followed by the current direction the rover is facing"
	print "Space separated, eg: '1 1 N'"
	error = 1
	while error == 1:
		
		error = 0
		current = raw_input("Current position and direction:")
		if " " in current:
			loc = locatechar(" ",current)
		else:
			error = 1
			if debug == True:
				print 1
		
		if current[len(current)-2] != " " and error == 0:
			error = 1
			if debug == True:
				print 2
		good = 0
		#check validity of direction
		for i in compass:
			if current[len(current)-1] == i and error == 0:
				good = 1
		if good == 0:
			error = 1
			if debug == True:
				print 3
		#check syntax of current coodinates
		
		try:
			cury = int(current[loc + 1:-2])
			curx = int(current[:loc])
		except:
			error = 1
			if debug == True:
				print 4
		if error == 0:
			curdir = current[len(current)-1]
		else:
			print "Invalid input. Please read instructions and try again."
	print "Finally, input the list of instructions you wish the rover to follow"
	print "eg: 'LMRM' interperites to 'turn left, move,turn right, move'"
	error = 1
	while error == 1:
		error = 0
		ins = raw_input("Instructions:")
		for i in ins:
			if i != "M" and i != "m" and i != "R" and i != "r" and i != "L" and i != "l":
				error = 1
		if error == 1:
			print "Invalid input. Please read instructions and try again."
	#start simulation
	for i in ins:
		#turning
		##right
		if i == "r" or i == "R":
			loop3 = -1
			for i in compass:
				loop3 = loop3 + 1
				if i == curdir:
					n = loop3 + 1
					nn = 1
			if nn != 1:
				print "Error: Invalid current direction"
			if n >= 4:
				n = 0
			curdir = compass[n]
		##left
		if i == "l" or i == "L": 
			loop3 = -1
			for i in compass:  
				loop3 = loop3 + 1
				if i == curdir:
					n = loop3 - 1
					nn = 1  
			if nn != 1:
				print "Error: Invalid current direction"
			if n <= -1:   
				n = 3
			if debug == True:
				print n
			curdir = compass[n]
		#move
		if i == "m" or i == "M":
			mtor = 1
			crash = 0
			if curdir == "N":
				for i in rovers:
					if i != 0:
						if cury + 1 == i[1]:
							crash = 1
				
				cury = cury + 1
				
			if curdir == "E":
			
				for i in rovers:
					if i != 0:
						if curx + 1 == i[0]:
							crash = 1
				
				curx = curx + 1

			if curdir == "S":
			
				for i in rovers:
					if i != 0:
						if cury - 1 == i[1]:
							crash = 1
				
				cury = cury - 1

			if curdir == "W":
			
				for i in rovers:
					if i != 0:
						if curx - 1 == i[0]:
							crash = 1
				curx = curx - 1
			if crash == 1:
				print "The rover crashed at " + str(curx) + "," + str(cury)


	rovers.append([curx,cury])
	print str(curx) + " " + str(cury) + " " + curdir
	loop2 = 1
	while loop2 == 1:
		goagn = raw_input("Move another rover (y/n)?")
		if goagn == "y" or goagn == "n":
			loop2 = 0
			if goagn == "n":
				loop = 0
		else:
			print "Please enter 'y' or 'n'"


