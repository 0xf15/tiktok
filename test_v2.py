from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time
from colorama import Fore, init, Style
sc = ["|", "/", "-", "\\", "|", "/", "-", "\\"]
init()
class Cliamer:
    def __init__(self,browser):
        self.browser = browser
        browser.get('https://www-useast1a.tiktok.com/signup/create-username?lang=en')
        self.done = 0
        self.rs = 0
        self.secend = 0
        self.done = 0
        
    def GET_PARMS(self,_browser):
        time.sleep(0.50)
        network_requests = _browser.execute_script("""
        var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {};
        var network = performance.getEntriesByType("resource");
        return network;
            """)
        done = False

        for request in network_requests:
            if("api/compliance/settings" in request["name"] ):
                parms = str(request["name"]).split("?")[1]
               
                done = True
                _browser.refresh() 
                return parms
        if(done == False):
            _browser.refresh() 
            return False
        
    def SeNd(self,user,parms):
        res = requests.options(f"https://www-useast1a.tiktok.com/api/uniqueid/check/?{parms}",data=f"unique_id={user}&aid=1988",headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",'Cookie': 'sessionid=b8572a01842d271cffe0e597cb0fb93f'}).text
        print(res)
        if("is_valid" in res):
            self.done +=1

            
    def go(self,user):
        parms = self.GET_PARMS(browser)
        if(parms):
            self.SeNd(user,parms)
browser = webdriver.Firefox()


Clim = Cliamer(browser)
def RsCount():
	while True:
		for s in sc:
			Clim.secend = Clim.done
			time.sleep(1)
			Clim.rs = Clim.done - Clim.secend
			print("{}{}[{}{}{}] Attempts: {:,} | R/S: {:,}".format(Style.BRIGHT, Fore.WHITE, Fore.RED, s, Fore.WHITE, Clim.done, Clim.rs), end="\r")
def gos():
        parms = Clim.GET_PARMS(browser)
        if(parms):
            for i in range(35):
                Thread(target=Clim.SeNd,args=("ksa",parms)).start()

Thread(target=RsCount).start()
while 1:
    gos()
    time.sleep(1)
input("2")