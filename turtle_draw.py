#!/usr/bin/env python3

import turtle

turtle.setup(800, 400)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("red")
turtle.seth(-40)
for i in range(4):
	turtle.circle(40,80)
	turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()
	
