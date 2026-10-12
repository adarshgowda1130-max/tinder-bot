from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
load_dotenv()
mail=os.getenv("mail")
password=os.getenv("password")
url=os.getenv("url")
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
user_data_der=os.path.join(os.getcwd(),"chrome_profile")
chrome_options.add_argument(f"--user-data-der--={user_data_der}")
driver=webdriver.Chrome(options=chrome_options)
driver.get(url=url)
wait=WebDriverWait(driver,10)


loginBtn=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/header/button')))
loginBtn.click()

facebook_login=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="login-modal"]/div/div/div/button[1]'))).click()
base_window=driver.window_handles[0]#window_handles opens the new window 
facebook_window=driver.window_handles[1]
driver._switch_to.window(facebook_window)
# print(driver.title)
email=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="email"]')))
email.send_keys(mail)
my_password=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="pass"]')))
my_password.send_keys(password)
facebook_submit=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/form/button')))
facebook_submit.click()
driver.switch_to.window(base_window)
b1=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/div/div/form/button'))).click()
b2=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/div/div/form/button[1]'))).click()
b3=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/div/div/form/button'))).click()
# pop_text=wait.until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/main/div[3]/h1')))
# print(pop_text.text)
for i in range(20):
    like_button2=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="like-button-container"]/form/button')))
    driver.execute_script("arguments[0].click();", like_button2)
driver.quit()
