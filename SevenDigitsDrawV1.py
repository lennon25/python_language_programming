#!/usr/bin/env python3

import turtle

# 绘制单个线段
def drawLine(draw):
	turtle.pendown() if draw else turtle.penup()
	turtle.fd(40)
	turtle.right(90)

# 绘制数字
def drawDigit(digit):
	drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
	drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
	drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
	drawLine(True) if digit in [0,2,6,8] else drawLine(False)
	turtle.left(90)
	drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
	drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
	drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
	turtle.left(180)
	turtle.penup()
	turtle.fd(30)

# 绘制日期
def drawDate(date):
	for i in date:
		drawDigit(eval(i))

def main():
	turtle.setup(800,350,200,200)
	turtle.penup()
	turtle.fd(-300)
	turtle.pensize(5)
	drawDate('20190825')
	turtle.hideturtle()
	turtle.done()

main()

