from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import datetime
import time


def open_website_and_login():
    driver.find_element(By.ID, "Email").send_keys("xavierguertin@gmail.com")
    driver.find_element(By.ID, "Password").send_keys("BotInProgress123!")

    # Find & Click on the login button
    driver.find_element(By.XPATH, '//input[@value="Se connecter"]').click()
    # Find & Click on the reservation button
    driver.find_element(By.XPATH, '//div[@id="btnsAccueil"]/a').click()
    # Find & Click on the 4th day available
    driver.find_element(By.XPATH, '//*[@id="formDate"]/div[2]/div[4]/a/div').click()
    # Find & Click on the tennis activity
    driver.find_element(By.XPATH, '//a[@href="/rtpeps/Reservation/Disponibilites?selectedActivite=Tennis"]').click()
    book_reservation_at_time(target_time)


def book_reservation_at_time(target_time_to_book):
    while True:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        if current_time >= target_time_to_book:
            # find booking spot & click on reservation
            xpath_expr = (f'//tr[td[2][normalize-space(.)="{target_time_short}"]]'
                          f'[td[4][normalize-space(.)="{courtLetter}"]]/td[5]/a')
            driver.find_element(By.XPATH, xpath_expr).click()
            # find my tennis partner
            dropdown = Select(driver.find_element(By.ID, "ddlPartenaire0"))
            dropdown.select_by_value("53450")
            # Confirm reservation
            WebDriverWait(driver, 2).until(ec.element_to_be_clickable((By.ID, "linkConfirmer"))).click()
            break
        if current_time < verify_time:
            time.sleep(5)  # check every 5 seconds


# Declare variables
courtLetter = 'C'  # court letter
target_time = '11:30:00'  # target time here

target_datetime = datetime.datetime.strptime(target_time, '%H:%M:%S')  # convert target_time to string with seconds
target_time_short = datetime.datetime.strptime(target_time, '%H:%M:%S').strftime('%H:%M')  # convert to string
# Subtract 10 seconds from the parsed datetime
verify_dateTime = target_datetime - datetime.timedelta(seconds=10)
verify_time = verify_dateTime.strftime('%H:%M:%S')  # convert to string

startTime = datetime.datetime.now()  # start timer
driver = webdriver.Edge()  # initialize driver to use Edge
driver.get('https://secure.sas.ulaval.ca/rtpeps/Account/Login')  # access desired web page
open_website_and_login()  # call function
stopTime = datetime.datetime.now()  # stop timer

# Calculate total seconds
seconds = int((stopTime - startTime).total_seconds())

# Format the string
totalTime = f"{seconds} sec"

# Save result to logs
file = open(r'C:\Users\Xavier\OneDrive - Concordia University - Canada\TennisBot\results\logs.txt', 'a')
file.write(f"{datetime.datetime.now()} - The script ran. Reservation was booked for "
           f"{(datetime.datetime.now() + datetime.timedelta(hours=70)).strftime('%Y-%m-%d ') + target_time_short}."
           f" The time taken for the bot was {totalTime} and it stopped at: {stopTime.strftime('%H:%M:%S')}.\n")
