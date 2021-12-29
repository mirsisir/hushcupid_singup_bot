from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.get("https://hushcupid.com/")
driver.get("http://localhost/social-dating")
over18Button = driver.find_element_by_xpath('//*[@id="agree-over18"]')
over18Button.click()

firstName = driver.find_element_by_xpath('//*[@id="name_first"]')
name = ''.join(random.choices(string.ascii_letters, k=5))
firstName.send_keys(name)

UserName = driver.find_element_by_xpath('//*[@id="username"]')
UserName.send_keys(name)

Email = driver.find_element_by_xpath('//*[@id="email"]')
Email.send_keys(name + '@gmail.com')

Password = driver.find_element_by_xpath('//*[@id="password"]')
Password.send_keys('12345678@Mir')

Submit = driver.find_element_by_xpath('//*[@id="form_join_user-element-11"]')
Submit.click()

Submit = driver.find_element_by_xpath('//*[@id="form_join_user-element-11"]/span')
Submit.click()

# Step 2
# i am
Submit = driver.find_element_by_xpath('//*[@id="form_join_user2-element-2"]/div/div[1]/table/tbody/tr/td[2]/label/span')
Submit.click()

# Looking for
female = driver.find_element_by_xpath(
    '//*[@id="form_join_user2-element-4"]/div/div[1]/table/tbody/tr/td[2]/label/span').click()

male = driver.find_element_by_xpath(
    '//*[@id="form_join_user2-element-4"]/div/div[2]/table/tbody/tr/td[2]/label/span').click()

# birthday

birthday = driver.find_element_by_xpath('//*[@id="birth_date"]')
birthday.send_keys("12121212")


time.sleep(4)
