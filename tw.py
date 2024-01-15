import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_autoinstaller as chromedriver


chromedriver.install()
wd = webdriver.Chrome()


url = "https://twitter.com/TTAgrup" #url you want to like
like_number = 10                    #the number of posts you want to like in the url
username = "username"               #your username here
password = "password"               #your password here


def Login(username,password):
    wd.get("https://twitter.com/login")
    time.sleep(3)
    wd.find_element(By.NAME,'text').send_keys(username)
    wd.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
    time.sleep(1)
    wd.find_element(By.NAME,'password').send_keys(password)
    wd.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()
 

def Like(url,like_number):
        wd.get(url)
        time.sleep(5)
        try:
            i = 0
            while i < 2:
                popUp = wd.find_element(By.XPATH,'//div[@data-testid="sheetDialog"]')
                if popUp is not None:
                    True
                    wd.find_elements(By.XPATH,'//div[@data-testid="app-bar-close"]')[0].click()
                    time.sleep(3)
                i += 1
        except:
            pass
        # while len(wd.find_elements(By.XPATH,'//div[@data-testid="like"]')) < 30:
        #     d = len(wd.find_elements(By.XPATH,'//div[@data-testid="like"]'))
        #     print(d)
        #     html = wd.find_element(By.TAG_NAME,'html')
        #     html.send_keys(Keys.END)
        #     time.sleep(12)

        time.sleep(1)
        
        like_count = 0
        while like_count < like_number:
            action = ActionChains(wd)
            btn = wd.find_elements(By.XPATH,'//div[@data-testid="like"]')[0]
            if btn is None:
                True
                break
            action.move_to_element(btn).click().perform()
            time.sleep(2)
            like_count = like_count + 1
            print(like_count)
            
        
def Logout():
    wd.get("https://twitter.com/logout")
    time.sleep(2)
    wd.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]').click()
    time.sleep(1)



Login(username,password)
time.sleep(2)
Like(url,like_number)
Logout()