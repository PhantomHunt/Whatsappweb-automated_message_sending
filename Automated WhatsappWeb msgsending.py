#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
import sys

driver = webdriver.Edge('C:\Windows\System32\MicrosoftWebDriver.exe')
  
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 20) 

print("***** WELCOME TO AUTOMATIC WHATSAPP MESSAGE SENDER APPLICATION *****\n\n")
print("Enter Name of Group or Person: ")
t=input()
target="\'"+t+"\'"
x_arg = '//span[contains(@title,' + target + ')]'
try:
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg))) 
    group_title.click()
except:
    print("Name not found") 
    sys.exit()
    
print("Sending message to",target)
print("Enter the automated message: ")
string = input()
strfancy=": "+string+" [Automated message from Python by Phantom]"

print("How many times you want the message to be printed?")
val=int(input())
  
inp_xpath = '//div[@class="_3u328 copyable-text selectable-text"]'
try:
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath))) 
except:
    print("Inputbox not found")
    sys.exit()
    
for i in range(val): 
    #input_box.send_keys(string + Keys.ENTER) #Only simple text
    stringmain=str(i+1)+strfancy
    input_box.send_keys(stringmain + Keys.ENTER)  
print("Messages Sent Successfully")


# In[ ]:





# In[ ]:




