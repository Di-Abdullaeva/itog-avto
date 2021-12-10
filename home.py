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

driver.execute_script("window.scrollBy(0, 600);") #скролл на 600 пикселей вниз


seleniumRuby_href = driver.find_element_by_css_selector('.post-160.product.type-product.status-publish.has-post-thumbnail.product_cat-selenium.product_tag-ruby.product_tag-selenium.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.instock.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a > h3')
seleniumRuby_href.click()

reviews_href = driver.find_element_by_css_selector('.reviews_tab > a')
reviews_href.click()

raiting_href = driver.find_element_by_css_selector('.comment-form-rating>p>span>.star-5')
raiting_href.click()

review = driver.find_element_by_id('comment')
review.send_keys("Nice book!")
name = driver.find_element_by_id('author')
name.send_keys("Di")
email = driver.find_element_by_id('email')
email.send_keys("di@mail.ru")

time.sleep(2)

submit = driver.find_element_by_id('submit')
submit.click()

time.sleep(5)
driver.quit()