import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("user-data-dir=whatsappBotTrial") 
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://web.whatsapp.com/')
WebDriverWait(driver,60).until(EC.presence_of_element_located(
            (By.XPATH, '//div[@class="_210SC"]')))

def Send(text,i):
	global driver
	send_msg = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")))
	send_msg.send_keys(text+Keys.ENTER)
	i.click()
	

user_data={}
def check(text,i,name,current):
	global user_data
	f = open('quest.txt') 
	quest = json.load(f) 
	f = open('ans.txt')
	ans=json.load(f)
	print(user_data)
	current.click()
	if(text.lower()=='stop' and name in user_data.keys()):
		del user_data[name]
	if(text.lower()=='start'):
		user_data[name]=0
		print(user_data)
		Send(quest[0],i)
		return
	if(name in user_data.keys()):

		if(text.lower() in ans[user_data[name]]):
			try:
				Send(quest[ans.index(text.lower())+1],i)
				temp=user_data[name]+1
				user_data[name]=temp
			except:
				if(user_data[name]==len(ans)-1):
					Send('Congrats you have finised\n You Have and IQ of 1000!',i)
					del user_data[name]
					return
					
			return
		
		else:
			Send('Wrong Answer Try again',i)
			return 



while True:
	chats=driver.find_elements_by_xpath('//div[@class="_210SC"]')
	print(len(chats))
	chats[0].click()
	for i in chats:

		try:
			unread=i.find_element_by_css_selector("span._31gEB")
			unreadNo=int((unread.text))
			print(unreadNo)
			if(unreadNo):
				textM=(i.text)
				textM=textM.split('\n')
				name=textM[0]
				text=textM[-2]
				print('\n\nname ',name+'\n','text ',text)
				i.click()
				check(text,chats[0],name,i)

				
				
		except:
			pass
	# time.sleep(0.3)