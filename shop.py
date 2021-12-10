from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select

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

username = driver.find_element_by_id('username')
username.send_keys("di@mail.ru")
password = driver.find_element_by_id('password')
password.send_keys("Di4433Di00")
time.sleep(2)

login_btn = driver.find_element_by_css_selector('[name="login"]')
login_btn.click()

shop_href = driver.find_element_by_link_text("Shop")
shop_href.click()

'''HTML_href = driver.find_element_by_link_text("HTML")
HTML_href.click()

kolvoElement = driver.find_elements_by_css_selector('[id="content"]>ul>li')
if len(kolvoElement) == 3:
    print("На странице 3 элемента!")
else:
    print("На странице не 3 элемента!")'''

'''sort = driver.find_element_by_tag_name("select")
sort_check = sort.get_attribute("value")
assert sort_check == "menu_order"
print(sort_check)

sortLowToHigh = driver.find_element_by_tag_name("select")
select = Select(sortLowToHigh)
select.select_by_value("price-desc")

sort = driver.find_element_by_tag_name("select")
sort_check = sort.get_attribute("value")
print(sort_check)

assert sort_check == "price-desc"'''

AndroidQuickStart_href = driver.find_element_by_css_selector('.post-169 h3')
AndroidQuickStart_href.click()

oldPrice = driver.find_element_by_css_selector('.price> del> span')
oldPriceText = oldPrice.text
newPrice = driver.find_element_by_css_selector('.price> ins> span')
newPriceText = newPrice.text
#Проверка значений цен
assert oldPriceText == "₹600.00"
assert newPriceText == "₹450.00"

bookCover = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
bookCover.click()

bookCoverClose = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
bookCoverClose.click()

'''#Добавили в корзину
addToBasket = driver.find_element_by_css_selector('[data-product_id="182"]')
addToBasket.click()

item = driver.find_element_by_css_selector('.cartcontents')
itemText = item.text
priceBasket = driver.find_element_by_css_selector('[id="wpmenucartli"]>a>.amount')
priceBasketText = priceBasket.text
#Проверка значений цен
#assert itemText == "1 item"
#assert priceBasketText == "₹180.00"

basket = driver.find_element_by_css_selector('.wpmenucart-contents')
basket.click()

time.sleep(2)
basket = driver.find_element_by_css_selector('.wpmenucart-contents')
basket.click()

#Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
subtotalPrice = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal>td>.woocommerce-Price-amount.amount"), "₹180.00"))
print(subtotalPrice)

#Используя явное ожидание, проверьте что в Total отобразилась стоимость
totalPrice = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total>td .woocommerce-Price-amount.amount"), "₹189.00"))
print(totalPrice)'''

time.sleep(3)
driver.quit()