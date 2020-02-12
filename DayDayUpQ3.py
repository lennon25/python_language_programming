#!/usr/bin/env python3

def dayUp(dayfactor):
	dayup = 1.0
	for i in range(365):
		if i % 7 in [6, 0]:
			dayup *= 1 - dayfactor
		else:
			dayup *= 1 + dayfactor
	print("工作日的力量: {:.3f}".format(dayup))


dayUp(0.01)
dayUp(0.005)


