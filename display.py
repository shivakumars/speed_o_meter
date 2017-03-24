import RPi.GPIO as GPIO
import time

LCD_RS=21
LCD_E=20
LCD_D4=12
LCD_D5=25
LCD_D6=24
LCD_D7=23
LCD_ON=15

LCD_WIDTH=16
LCD_CHR=True
LCD_CMD=False

LCD_LINE_1=0x80
LCD_LINE_2=0xC0


GPIO.setmode(GPIO.BCM)
GPIO.setup(LCD_E, GPIO.OUT)
GPIO.setup(LCD_RS, GPIO.OUT)
GPIO.setup(LCD_D4, GPIO.OUT)
GPIO.setup(LCD_D5, GPIO.OUT)
GPIO.setup(LCD_D6, GPIO.OUT)
GPIO.setup(LCD_D7, GPIO.OUT)

GPIO.output(LCD_RS, LCD_CHR)

GPIO.output(LCD_E, True)


message="---------------------"

for i in range(LCD_WIDTH):
	if ord(message[i])&0x01==0x01:
		GPIO.output(LCD_D4, True)

GPIO.cleanup()