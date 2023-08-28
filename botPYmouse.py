from collections.abc import Callable, Iterable, Mapping
# from lib2to3.pgen2.driver import Driver
import time
import threading
from typing import Any
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

## Código com o clique apenas em cima 
delay = 5
button = Button.left
start_stopKey = KeyCode(char='a')
stopKey = KeyCode(char='b')

class Click(threading.Thread):
    def __init__(self, delay, button):
        super(Click, self).__init__()
        self.delay = delay
        self.button = button
        self.running = True
        self.programRun = True

    def start_click(self):
        self.running = True
        
    def stop_click(self):
        self.running: False
        
    def exit(self):
        self.stop_click()
        self.programRun = False

    def run(self):
        while self.programRun:
            mouse.click(self.button)
            time.sleep(self.delay)
        time.sleep(0.1)

mouse = Controller()
click_thread = Click(delay, button)
click_thread.start()

chromedriver_path = ChromeDriverManager().install()

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://127.0.0.1:3000/index.html')

elemento = driver.find_element_by_id('reload-button')
elemento.click()

def pressOn(key):
    if key == start_stopKey:
        if click_thread.running:
            click_thread.stop_click()
        else:
            click_thread.start_click()

    elif key == stopKey:
        click_thread.exit()
        listener.stop()

with Listener(on_press=pressOn) as listener:
    listener.join()

driver.quit()