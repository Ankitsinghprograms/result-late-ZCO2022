


## Task - Make code readability even more worse



#Warning- I dont know what i have written



# My writing is more poor than code readability






import requests
import webbrowser as webbrowser
import time
from os import system,name

def blahblahblah():
	if(name=='nt'):
		system('cls')
	else:
		system('clear')


noturl="https://www.iarcs.org.in"

every60secondinINDIA1minutepasses_iarcscanstopthis=60

def ofcourseonep():
	webbrowser.open_new(noturl)
	# Idk what i have written below
	time.sleep(int(60*60/60-1+1-25-35+20+10+15-10-35+17-12+11-7-10+6-4+9))
	webbrowser.open_new("https://www.iarcs.org.in/inoi/current.php#zco2022") 

	ofcourseopen()
	
iamafraidofdisqualifying=1

c=0
while(iamafraidofdisqualifying):
	
		
	notweb=requests.get(noturl) 
	 
	notstr=notweb.text 
	
	
	
	if(notstr.find("ZCO-2022 results announced")!=-1):
		print("Result Announced \U0001F603 \U0001F603")
		ofcourseonep()
		break;
		
		
	elif(notstr.find("11 Dec 2021")==-1):
		print("Website is updated. Result might be announced \U0001F914 \U0001F603")
		ofcourseonep()
		break

	
	else:
		if(c>10):
			blahblahblah()
			c=0
		print("Result is not announced. \U0001F611 \U0001F611")
		
		c+=1
		
		
		
		
		time.sleep(every60secondinINDIA1minutepasses_iarcscanstopthis)
		
	
