from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
from PIL import Image
import os
import shutil
import time
import private

def check_size(filename):
    size = os.path.getsize(filename)
    print(size)
    return size

def check_all_sizes(filesize, sizelist):
    for size in sizelist:
        if filesize == size:
            return True
    return False

def crop_image(filename):
    image = Image.open(filename)
    box = (0,0,1920,1080)
    cropped = image.crop(box)
    cropped.save(filename)

geckopath= "/usr/local/bin/geckodriver"

url = "http://preview.risevision.com/Viewer.html?type=display&id={}".format(private.displayid)
try:
    display = Display(visible=0, size=(1920,1080))
    display.start()

    options = Options()
    options.set_headless(headless=True)
    options.add_argument('-height 1080')
    options.add_argument('-width 1920')

    driver = webdriver.Firefox(options = options, capabilities={'ignoreZoomSetting':True})
    driver.get(url)
    time.sleep(5)

    driver.find_element_by_tag_name('html').send_keys(Keys.CONTROL, '-')
    driver.find_element_by_tag_name('html').send_keys(Keys.CONTROL, '-')
    driver.find_element_by_tag_name('html').send_keys(Keys.CONTROL, '-')


    shutil.rmtree('./tmp')
    os.makedirs('tmp')
    sizelist = []
    pictureCount = 0
    dupeCount = 0
    isDupe = False
    
    while dupeCount < private.threshhold:
        filename = "tmp/test{}.png".format(str(pictureCount))
        driver.save_screenshot(filename)
        newfilesize = check_size(filename)
        if newfilesize < 700000:
            os.remove(filename)
        if pictureCount is not 0:
            isDupe = check_all_sizes(newfilesize,sizelist)
        if isDupe:
            print(filename +" is duplicate, deleting,")
            dupeCount +=1
            os.remove(filename)
        else:
            sizelist.append(newfilesize)
            crop_image(filename)
        pictureCount+=1
        time.sleep(5)
finally:
    driver.close()
    display.stop()
    
"""
browser = b.get_browser(url)
assert 'Google' in browser.title

search = browser.find_element_by_id("lst-ib")
submit = browser.find_element_by_name("btnK")

search.send_keys('gnu/linux')
time.sleep(0.3)
submit.click()
time.sleep(0.5)
browser.save_screenshot("test.png")
browser.quit()
"""
