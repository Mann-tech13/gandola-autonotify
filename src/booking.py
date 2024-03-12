from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import schedule
import time
import sys
import notify

# This program has been used to notify on personal basis. Some customization in logic may be needed as per situation

def check_for_slots():
    driver = webdriver.Chrome()
    try:   

        # Make an instance of given website
        driver.get('https://jkcablecar.payu.in/')

        # To select phase 1 time slot booking (for 2nd phase, change @value='3')
        phase1_radio = driver.find_element("xpath", "//input[@value='1']")
        phase1_radio.click()

        time.sleep(2)

        # Finds and opens calendar
        date_input = driver.find_element("xpath", "//input[@class='visitcalendar']")
        date_input.click()

        # Custom logic to move to next month (To check for certain month, this logic can be handled differently)
        swtich_to_april = "document.getElementsByClassName('next')[0].click()"
        driver.execute_script(swtich_to_april)

        # To select date of particular month (x can be [0, 1, ...])
        date_script = "document.getElementsByClassName('day')[x].click();"
        driver.execute_script(date_script)

        # Check if window for booking has been opened or not
        select_slot = "document.getElementsByClassName('toast toasty-type-error toasty-theme-bootstrap')"
        toast_element = driver.execute_script("return " + select_slot)

        # if window has been opened then shoot mail
        if(len(toast_element) == 0):
            if(notify.send_mail()):
                sys.exit()
        time.sleep(5)
    finally:    
        driver.quit()


# Run for every 20 minutes
schedule.every(20).minutes.do(check_for_slots)

while True:
    schedule.run_pending()
  
