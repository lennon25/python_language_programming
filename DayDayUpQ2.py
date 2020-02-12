#!/usr/bin/env python3

def dayUp(dayfactor):
	dayup = pow(1 +dayfactor, 365)
	daydown = pow(1 - dayfactor, 365)
	print("Up: {:.3f}, Down: {:.3f}".format(dayup, daydown))


dayUp(0.005)
dayUp(0.01)