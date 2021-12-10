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

shop_href = driver.find_element_by_link_text("Shop")
shop_href.click()

driver.execute_script("window.scrollBy(0, 300);") #скролл на 300 пикселей вниз

#Добавили в корзину
addToBasketHTML = driver.find_element_by_css_selector('[data-product_id="182"]')
addToBasketHTML.click()
time.sleep(2)

'''addToBasketJS = driver.find_element_by_css_selector('[data-product_id="180"]')
addToBasketJS.click()'''

#Переход в корзину
basket = driver.find_element_by_css_selector('.wpmenucart-contents')
basket.click()


'''time.sleep(2)
deleteHTML = driver.find_element_by_css_selector('[data-product_id="182"]')
deleteHTML.click()

undo_href = driver.find_element_by_link_text("Undo?") #Нажмите на Undo (отмена удаления)
undo_href.click()

JSquantity = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")))
JSquantity[0].clear()
JSquantity[0].send_keys('3')

updateBasket_btn = driver.find_element_by_css_selector('[value="Update Basket"]')
updateBasket_btn.click()'''


'''#Нажмите на кнопку "Apply Coupon"
time.sleep(3)

applyCoupon_btn = driver.find_element_by_css_selector('[name="apply_coupon"]')
applyCoupon_btn.click()

#Добавьте тест, что возникло сообщение : "Please enter a coupon code."
txtCouponCode = driver.find_element_by_css_selector('.page-content.entry-content li')
txtCouponCodeText = txtCouponCode.text
print(txtCouponCodeText)
assert txtCouponCodeText == "Please enter a coupon code."'''

'''item = driver.find_element_by_css_selector('.cartcontents')
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

#Нажмите "PROCEED TO Checkout"
time.sleep(2)
proceed_href = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class='checkout-button button alt wc-forward']")))
#proceed_href = driver.find_element_by_css_selector("[class='checkout-button button alt wc-forward']")
proceed_href.click()

FirstName = wait.until(EC.presence_of_element_located((By.ID, "billing_first_name")))
FirstName.send_keys("Di")
LastName = driver.find_element_by_id("billing_last_name")
LastName.send_keys("Krasotka")
Email = driver.find_element_by_id("billing_email")
Email.send_keys("di@mail.ru")
Phone = driver.find_element_by_id("billing_phone")
Phone.send_keys("79253557500")

Country = driver.find_element_by_id("select2-chosen-1")
Country.click()
CountryText = driver.find_element_by_id("s2id_autogen1_search")
CountryText.send_keys("Russia")

selectCountry = driver.find_element_by_css_selector('[class="select2-match"]')
selectCountry.click()
'''selectCountry = driver.find_element_by_id("select2-results-1")
select = Select(selectCountry)
select.select_by_visible_text("Russia")'''

Address = driver.find_element_by_id("billing_address_1")
Address.send_keys("Prospekt mira, 7")
City = driver.find_element_by_id("billing_city")
City.send_keys("Moscow")
State = driver.find_element_by_id("billing_state")
State.send_keys("Moscow")
Zip = driver.find_element_by_id("billing_postcode")
Zip.send_keys("163077")

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
checkPayments = driver.find_element_by_css_selector('[value="cheque"]')
checkPayments.click()

time.sleep(2)
placeOrder_btn = driver.find_element_by_id("place_order")
placeOrder_btn.click()

orderReceived = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class='woocommerce-thankyou-order-received']"), "Thank you. Your order has been received."))
print(orderReceived)
PaymentMethod = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class='woocommerce-thankyou-order-details order_details'] .method>strong"), "Check Payments"))
print(PaymentMethod)

time.sleep(3)
driver.quit()