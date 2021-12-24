import pyautogui
import time

words = open("message.txt", 'r')
time.sleep(5)

for word in words:
    for char in word:
        pyautogui.typewrite(char)
    time.sleep(1)


# for i in range(10):
#     pyautogui.typewrite('word')
#     pyautogui.press('enter')
#     time.sleep(0.7)
