from selenium import webdriver		
from selenium.webdriver.chrome.options import Options		
from selenium.webdriver import ActionChains		
from selenium.webdriver.common.keys import Keys		
from selenium.webdriver.support.ui import WebDriverWait		
from selenium.webdriver.common.action_chains import ActionChains		
from selenium.webdriver.common.by import By		
from selenium.webdriver.support import expected_conditions as EC		
from selenium.webdriver.common.by import By		
from time import sleep		
import string		
import random		
import copy		
import sys		
import subprocess		
import zipfile		
from config import	mail91	
from config import	mail92	
from config import	mail93	
from config import	mail94	
from config import	mail95	
from config import	mail96	
from config import	mail97	
from config import	mail98	
from config import	mail99	
from config import	mail100	
from config import password		
#from scmining import script		
#PROXY = "socks5://159.223.88.53:33333"		
options = webdriver.ChromeOptions()		
options.add_experimental_option("excludeSwitches", ["enable-automation"])		
options.add_experimental_option('useAutomationExtension', False)		
options.add_argument('--disable-blink-features=AutomationControlled')		
options.add_argument("--window-size=600,700")		
#options.add_argument('--proxy-server=%s' % PROXY)		
#options.add_extension('anticaptcha-plugin_v0.62.zip')		
driver = webdriver.Chrome(options=options)		
sleep(1)		
driver.implicitly_wait(1200) # seconds		
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(	mail91	)
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()		
sleep(0.5)		
driver.implicitly_wait(1200) # seconds		
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(	mail92	)
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()		
sleep(0.5)		
driver.implicitly_wait(1200) # seconds		
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(	mail93	)
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()		
sleep(0.5)		
driver.implicitly_wait(1200) # seconds		
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(	mail94	)
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()		
sleep(0.5)		
driver.implicitly_wait(1200) # seconds		
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(	mail95	)
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()		
sleep(0.5)		
driver.implicitly_wait(1200) # seconds		
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(	mail96	)
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()		
sleep(0.5)		
driver.implicitly_wait(1200) # seconds		
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(	mail97	)
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()		
sleep(0.5)		
driver.implicitly_wait(1200) # seconds		
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(	mail98	)
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()		
sleep(0.5)		
driver.implicitly_wait(1200) # seconds		
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(	mail99	)
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()		
sleep(0.5)		
driver.implicitly_wait(1200) # seconds		
driver.get("https://accounts.google.com/AddSession?service=accountsettings&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue&ec=GAlAwAE")		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]').send_keys(	mail100	)
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()		
sleep(0.5)		
driver.find_element(by=By.XPATH, value='//*[@id="confirm"]').click()		
sleep(0.5)		
