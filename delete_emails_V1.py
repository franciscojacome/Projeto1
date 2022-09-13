import pyperclip
import pyautogui
import time


# Abrir o Google Chrome
with pyautogui.hold(['command']):
    time.sleep(1)
    pyautogui.press('space')
pyautogui.write("Google")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)

# Acessar site
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

# Pesquisar o remetente desejado
pyautogui.click(x=331, y=112)
pyautogui.write("investidor@levanteinvestimentos.com")
pyautogui.press("enter")
time.sleep(1)

# Selecionar todos os e-mails
pyautogui.click(x=282, y=221)
time.sleep(1)
pyautogui.click(x=1022, y=272)
time.sleep(1)
pyautogui.click(x=429, y=220)
time.sleep(1)
pyautogui.click(x=1032, y=589)
time.sleep(1)

# Exluir definitivamente
pyautogui.click(x=57, y=594)
time.sleep(1)
pyautogui.click(x=110, y=753)
time.sleep(1)
pyautogui.click(x=282, y=221)
time.sleep(1)
pyautogui.click(x=1089, y=276)
time.sleep(1)
pyautogui.click(x=396, y=224)
time.sleep(1)
pyautogui.click(x=1029, y=618)