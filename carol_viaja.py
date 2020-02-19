import datetime
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from pyvirtualdisplay import Display

options = Options()
options.headless = True

today = datetime.date.today()

def train_table_dict(dep="Porto - Sao Bento", arr="Braga"):
    file = f'./timetables/{dep}-{arr}_{today.month}{today.day}.html'
    print(file)
    if os.path.exists(file):
        print("O ficheiro existe!")
        return file
    else:
        print("Vamos levantar a informação!")
        retrieve_train(dep, arr)
        return file


def retrieve_train(dep="Porto - Sao Bento", arr="Braga"):
    display = Display(visible=0, size=(800, 600))
    display.start()
    browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
    browser.get('http://cp.pt')
    x = browser.find_element_by_name("depart")
    x.click()
    x.send_keys(dep)
    y = browser.find_element_by_name("arrival")
    y.send_keys(arr)
    x.submit()
    time.sleep(2)
    ttable = browser.find_element_by_class_name("table-search-results")
    with open(f'./timetables/{dep}-{arr}_{today.month}{today.day}.html', 'w') as f:
        for i in ttable.text:
            f.write(i)
    browser.close()
