from selenium import webdriver  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.chrome.service import Service  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore
from selenium.webdriver.support import expected_conditions as EC  # type: ignore
import time
from datetime import datetime, timedelta

# Path to chromedriver
chromedriver_path = 'C:/chromedriver/chromedriver-win64/chromedriver.exe'  # Replace with your chromedriver path

# Configure ChromeDriver service
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)


# Function to get the desired date in 'dd/mm/yyyy' format
def get_future_date(days_to_add):
    future_date = datetime.now() + timedelta(days=days_to_add)
    return future_date.strftime("%d/%m/%Y")  # Date format matching the 'data-day' attribute format

# Open the webpage
driver.get('https://deportesweb.madrid.es/DeportesWeb/login')


# Wait until the "Email and password" button is visible (maximum 10 seconds)
try:
    # Click the "Email and password" button
    email_password_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h4[text()='Correo y contraseña']"))
    )
    email_password_button.click()

    # Wait for input fields to be available
    time.sleep(1)  # Wait a bit for the new page to load

    # Enter email
    email_input = driver.find_element(By.ID, "ContentFixedSection_uLogin_txtIdentificador")  # Email field ID
    email_input.send_keys("xxxxxx")  # Replace with your email

    # Enter password
    password_input = driver.find_element(By.ID, "ContentFixedSection_uLogin_txtContrasena")  # Password field ID
    password_input.send_keys("xxxxxx")  # Replace with your password

    # Click the login button
    login_button = driver.find_element(By.ID, "ContentFixedSection_uLogin_btnLogin")  # Login button ID
    login_button.click()
    time.sleep(1)

    # Click the "Multitraining Room" button
    multitraining_room_button = driver.find_element(By.XPATH, "//h4[@title='Sala multitrabajo']")
    multitraining_room_button.click()
    time.sleep(1)

    # Click the "Aluche" button. Replace with your Gym Center
    aluche_button = driver.find_element(By.XPATH, "//h4[@class='media-heading' and text()='Aluche']")
    aluche_button.click()
    time.sleep(1)

    # Click on the day 16 on the calendar. Replace with the day you want to book
    calendar_day = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div[3]/div[3]/div[2]/div/div[4]/div[2]/div/ul/li[1]/div/div[1]/table/tbody/tr[3]/td[4]")
    calendar_day.click()
    time.sleep(3)

    # Click the 20:00 time slot. Replace with the hour you want to book
    time_slot_2000 = driver.find_element(By.XPATH, "//h4[@class='media-heading' and text()='20:00']")
    time_slot_2000.click()
    time.sleep(3)

    # Click the confirm purchase button
    confirm_purchase_button = driver.find_element(By.ID, "ContentFixedSection_uCarritoConfirmar_btnConfirmCart")
    confirm_purchase_button.click()

    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
