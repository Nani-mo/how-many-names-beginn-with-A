print("It's a trap")
import time
import random
from faker import Faker
fake = Faker()

Counter=0

def operation():
	counter = 0
	cycles = int(input("Anzahl der Durchlaeufe (nur Ganzzahlen): "))
	letterToSearch = str(input("Anfanhsbuchstabe nach dem gesucht werden soll: "))
	for n in range(cycles):
		name = fake.name()
		letter = (name[0])
		if letter == letterToSearch:
			counter = counter + 1
			print (counter)
	
	counterDurchCycles = counter / cycles
	Anteil = counterDurchCycles * 100
	Anteil = float(Anteil)
	print("\nvon " + str(cycles) + " random Namen begannen " + str(counter) + " mit einem '" + letterToSearch + "'")
	print(str(round(Anteil, 2)) + "% der Gesammtmänge beginnen mit '" + letterToSearch + "'")

operation()
useless = str(input("\nEnter zum beenden"))