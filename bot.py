from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import datetime
import time


def open_website_and_login():
    time.sleep(1)
    if driver.find_element(By.ID, "Email-error").size != 0:
        driver.find_element(By.ID, "Email").send_keys("xavierguertin@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("bot")

    # Find & Click on the login button
    driver.find_element(By.XPATH, '//input[@value="Se connecter"]').click()
    # Find & Click on the reservation button
    driver.find_element(By.XPATH, '//div[@id="btnsAccueil"]/a').click()
    # Find & Click on the 4th day available
    driver.find_element(By.XPATH, '(//div[@class="square"]/a)[4]').click()
    # Find & Click on the tennis activity
    driver.find_element(By.XPATH, '//a[@href="/rtpeps/Reservation/Disponibilites?selectedActivite=Tennis "]').click()
    book_reservation_at_time(target_time)


def book_reservation_at_time(target_time_to_book):
    while True:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        if current_time >= target_time_to_book:
            # find booking spot & click on reservation
            xpath_expr = f'(//td[normalize-space(text())="{target_time_short}"])[6]/following-sibling::td/a'
            driver.find_element(By.XPATH, xpath_expr).click()
            # find my tennis partner
            dropdown = Select(driver.find_element(By.ID, "ddlPartenaire0"))
            dropdown.select_by_value("53450")
            # Confirm reservation
            driver.find_element(By.ID, "linkConfirmer").click()
            break
        if current_time < verify_time:
            time.sleep(5)  # check every 5 seconds


target_time = '20:30:00'  # target time here
target_datetime = datetime.datetime.strptime(target_time, '%H:%M:%S')
target_time_short = datetime.datetime.strptime(target_time, '%H:%M')
# Subtract 10 seconds from the parsed datetime
verify_dateTime = target_datetime - datetime.timedelta(seconds=10)
verify_time = verify_dateTime.strftime('%H:%M:%S')

startTime = datetime.datetime.now()
driver = webdriver.Edge()
driver.get('https://secure.sas.ulaval.ca/rtpeps/Account/Login')
open_website_and_login()
stopTime = datetime.datetime.now()

# Calculate total seconds
total_seconds = int((stopTime - stopTime).total_seconds())

# Calculate minutes and seconds
minutes = total_seconds // 60
seconds = total_seconds % 60

# Format the string
totalTime = f"{minutes} min and {seconds} sec"

# Save Result to Logs
file = open(r'C:\Users\Xavier\OneDrive - Concordia University - Canada\TennisBot\results\logs.txt', 'a')
file.write(f"{datetime.datetime.now()} - The script ran. Reservation was booked for "
           f"{(datetime.datetime.now() + datetime.timedelta(hours=70)).strftime('%Y-%m-%d %H:%M')}."
           f" The time taken for the bot was {totalTime}")
