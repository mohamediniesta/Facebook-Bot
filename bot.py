#coding:utf-8
from selenium.webdriver.common.keys import Keys
import sys
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from datetime import datetime
def lettre(chaine,temp):
    for l in chaine:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(temp)
welcome = "   Welcome Mr OWNER \n \n"
lettre(welcome,0.03)
print "{0} Starting Firefox ".format(datetime.now())
driver = webdriver.Firefox()
driver.maximize_window()
print "{0} Connecting to https://www.facebook.com".format(datetime.now())
driver.get("https://www.facebook.com")
user = driver.find_element_by_css_selector('#email')
user.send_keys('Your_EMAIL') #Email
password = driver.find_element_by_css_selector('#pass')
password.send_keys("Your_PASSWORD") #Password
button = driver.find_element_by_css_selector('#u_0_3')
button.submit()
time.sleep(5)
print " Email : ",
lettre(" username",0.02) #email affichage
print "\n Password : ",
lettre(" Pass here \n \n",0.02) #password affichage
driver.get("https://www.facebook.com/messages/t/username")
print " Waiting ",
lettre("......",0.2)
demarre = False
while 1==1:
    stop = False
    source = driver.page_source
    soup = BeautifulSoup(source,'html.parser')
    a = soup.find("span",{"class":"_3oh-"})
    message = soup.findAll("span",{"class":"_3oh- _58nk"})
    longeur = len(message)-1
    if message[longeur].text == 'exit':
        exit(0)
        driver.quit()
    if message[longeur].text == "stop":
        print " Waiting ",
        lettre("......",0.2)
        demarre = False
        stop = True
    if message[longeur].text == 'robot':
        if demarre == False:
            print "\n Ok Sir ! "
            demarre = True
            stop = False
    while(demarre == True and stop == False):
        for i in range(2):
            driver.find_element_by_xpath('//*[@title="Envoyer une mention J’aime"]').click()
            time.sleep(0.1)
            print "Smiley {0} send to {1}".format(i+1,a.text)
            stop = True
    time.sleep(0.2)
driver.quit()
