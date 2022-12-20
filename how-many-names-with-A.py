print("It's a trap")
from faker import Faker #import the library faker for the random names
fake = Faker()

Counter=0

#main function
def operation():
	counter = 0
	cycles = int(input("Anzahl der Durchlaeufe (nur Ganzzahlen): ")) #input of the grand letter and how many cycles the loop should be
	letterToSearch = str(input("Anfanhsbuchstabe nach dem gesucht werden soll: "))
	for n in range(cycles): #loop for [cycles] times
		name = fake.name()
		letter = (name[0])
		if letter == letterToSearch:
			counter = counter + 1
			print (counter)
	
	counterDurchCycles = counter / cycles #calculate the percentage
	Anteil = counterDurchCycles * 100
	Anteil = float(Anteil)
	print("\nvon " + str(cycles) + " random Namen begannen " + str(counter) + " mit einem '" + letterToSearch + "'") #output the result
	print(str(round(Anteil, 2)) + "% der Gesammtmänge beginnen mit '" + letterToSearch + "'")

operation()
useless = str(input("\nEnter zum beenden"))

