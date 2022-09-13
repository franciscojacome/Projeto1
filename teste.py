from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip
import pyautogui
import time

# Definir caminho para executar o ChromeDriver
driver = webdriver.Chrome(executable_path=r'./chromedriver')

# Caminho padrao
driver = webdriver.Chrome()
# driver.get('https://accounts.google.com/v3/signin/identifier?dsh=S-989770824%3A1662995428673017&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Ftab%3Drm%26ogbl&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Ftab%3Drm%26ogbl&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWoN38B56mpUaFfVP6tXXpN3BRF873d0lqIqDKZ3Ng3VMfsySt0UZd5hUwIwnezMas9fyBWafQ#inbox')

with pyautogui.hold(['command']):
    time.sleep(1)
    pyautogui.press('space')
pyautogui.write("Google")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)

with pyautogui.hold(['command']):
    time.sleep(1)
    pyautogui.press('t')
time.sleep(1)
pyperclip.copy("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
with pyautogui.hold(['command']):
    time.sleep(1)
    pyautogui.press('v')
time.sleep(1)
pyautogui.press("enter")
time.sleep(2)
email = driver.find_element(By.ID, "aso_search_form_anchor")
email.clear()
email.send_keys("franciscoruiz697@gmail.com")
# with pyautogui.hold(['command']):
#     time.sleep(1)
#     pyautogui.press('v')
# time.sleep(1)
# pyautogui.press("enter") 
# time.sleep(2)
# email = driver.find_element(By.ID, "identifierId")
# email.clear()
# email.send_keys("franciscoruiz697@gmail.com")
# email.send_keys(Keys.RETURN)


# senha do Google: mvouwurteoqeawyd

#passwd = driver.find_element(By.ID, "pass")
#passwd.clear()
#passwd.send_keys("P")
#passwd.send_keys(Keys.RETURN)


#assert "No results found." not in driver.page_source




