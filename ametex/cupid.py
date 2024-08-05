from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the website
driver.get("https://www.example.com Wait for the element with id "myElement" to be clickable
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "myElement"))
)

# Perform an action on the element
element.click()

# Close the browser
driver.quit()
