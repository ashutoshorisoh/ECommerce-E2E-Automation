import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.implicitly_wait(3)
wait=WebDriverWait(driver, 10)

shop_btn = driver.find_element(By.XPATH, "//a[normalize-space()='Shop']")
shop_btn.click()

add_cart = driver.find_element(By.XPATH, "//app-card-list[@class='row']/app-card[1]/div/div[@class='card-footer']/button")
add_cart.click()

checkout_btn= driver.find_element(By.XPATH, "//a[contains(text(), 'Checkout')]")
checkout_btn.click()

finalCheckoutBtn = driver.find_element(By.XPATH, "//button[contains(text(), 'Checkout')]")
finalCheckoutBtn.click()

country_input = driver.find_element(By.XPATH, "//input[@id='country']")
country_input.send_keys("Ind")

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='suggestions']/ul/li/a[contains(text(),'India')]")))
country_select = driver.find_element(By.XPATH, "//div[@class='suggestions']/ul/li/a[contains(text(),'India')]")
country_select.click()

termsAgree = driver.find_element(By.XPATH, "//label[@for='checkbox2']")
termsAgree.click()

purchaseClick = driver.find_element(By.XPATH, "//input[@value='Purchase']")
purchaseClick.click()

successMessage =(By.XPATH, "//div/strong")
element = wait.until(expected_conditions.visibility_of_element_located(successMessage))

assert element.is_displayed(), "error is succes message"
print("sucees process")

time.sleep(2)
driver.close()