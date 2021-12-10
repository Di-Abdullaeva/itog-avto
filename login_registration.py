from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

path_to_extension = r'C:\Users\Диана\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.40.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension='+ path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
time.sleep(10)
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.get("http://practice.automationtesting.in/")

myAccount_href = driver.find_element_by_link_text("My Account")
myAccount_href.click()

'''regEmail = driver.find_element_by_id('reg_email')
regEmail.send_keys("di@mail.ru")
regPassword = driver.find_element_by_id('reg_password')
regPassword.send_keys("Di4433Di00")
time.sleep(2)
register_btn = driver.find_element_by_css_selector('[name="register"]')
register_btn.click()'''

username = driver.find_element_by_id('username')
username.send_keys("di@mail.ru")
password = driver.find_element_by_id('password')
password.send_keys("Di4433Di00")
time.sleep(2)

login_btn = driver.find_element_by_css_selector('[name="login"]')
login_btn.click()

logout_href = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation> ul>.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout>a"), "Logout"))
print(logout_href)

time.sleep(3)
driver.quit()