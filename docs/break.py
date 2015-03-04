Gradecounter=0
totals=0

while 1:
	grade=raw_input('Enter the grade or -1 to end: ')
	grade=int(grade)

	if grade==-1:
		break

	totals+=grade
	Gradecounter+=1
if Gradecounter!=0:
	avearage=float(totals)/Gradecounter
	print'The avearage is:',avearage
else:
	print'No grades where entered:'


	