from collections.abc import Callable, Iterable, Mapping
import time
import threading
from typing import Any
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

delay = 2 # 2 segundos
button = Button.left
start_stopKey = KeyCode.from_char('a')
stopKey = KeyCode.from_char('b')

class Click(threading.Thread):
    def __init__(self, delay, driver):
        super(Click, self).__init__()
        self.delay = delay
        self.driver = driver
        self.running = threading.Event()
        self.running.set()  # Inicializa como True
        self.button = button
        self.programRun = True

    def start_click(self):
        self.running.set()
        
    def stop_click(self):
        self.running.clear()
        
    def exit(self):
        self.stop_click()
        self.programRun = False

    def run(self):
        while self.programRun:
            if self.running:
                self.driver.execute_script("arguments[0].click();", elemento)
                time.sleep(self.delay)

mouse = Controller()

driver = webdriver.Chrome()

driver.get('url.teste.com.br')
wait = WebDriverWait(driver, 10)

# find_element_by_class_name = classe
# find_element_by_tag_name('div')[1] = div, a, input, etc
# elemento = driver.find_element(By.CSS_SELECTOR, 'seletor-css-aqui') = css
elemento = wait.until(EC.visibility_of_element_located((By.ID, 'id-teste')))
elemento.click()

click_thread = Click(delay, driver)
click_thread.start()

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
