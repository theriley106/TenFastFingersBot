import Image
import pytesseract
import pyautogui
import time

##You're probably going to have to edit the crop regions depending on your screen resolution
def DetectAddress():
	pyautogui.screenshot('dssdfs.png', region=(175,60,175+800,60+27))
	img = Image.open('dssdfs.png')
	img = img.crop((175,60,(175+800),(60+22)))
	img.save('dssdfss.png')
	Address = pytesseract.image_to_string(Image.open('dssdfss.png'))
	if 'fast' in Address:
		print(Address)
		return True
	else:
		print(Address)
		return False
	
	
def TypingCompetition():
	while DetectAddress() is False:
		time.sleep(3)
	t_end = time.time() + 60
	while time.time() < t_end:
		img = pyautogui.screenshot('screen.png')
		img = img.crop((425,250,(425) + 1000,(250) + 50))
		
		img.save('screen.png')
		SS = pytesseract.image_to_string(Image.open('screen.png'))
		SS = SS.split(' ')
		for words in SS:
			pyautogui.typewrite("{} ".format(words))
			time.sleep(.05)

def AntiCheat():
	a = input('Start in Y')
	time.sleep(2)
	pyautogui.screenshot('dssdfs.png')
	img = Image.open('dssdfs.png')
	img = img.crop((580,275,(580+600),(275+200)))
	img.save('screen.png')
	SS = pytesseract.image_to_string(Image.open('screen.png'))
	SS = SS.split(' ')
	for words in SS:
		pyautogui.typewrite("{} ".format(words))

	pyautogui.press('tab')
	time.sleep(.5)
	pyautogui.press('enter')
