from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import osm_login
option=Options()
option.add_argument("--window-size=1920,1080")
browser=webdriver.Chrome(options=option)
browser.delete_all_cookies()
browser.get("https://en.onlinesoccermanager.com/Login")
browser.implicitly_wait(5)
sleep(2)
#ilk ekran
ilk=browser.find_element(By.XPATH,"//*[@id='page-privacynotice']/div/div/div[2]/div[3]/div/button")
ilk.click()
cg=browser.find_element(By.XPATH,"//*[@id='page-signup']/div[3]/div[4]/div[2]/button")
cg.click()

#login
kullanıcı_adı=browser.find_element(By.XPATH,"//*[@id='manager-name']")
kullanıcı_adı.send_keys(osm_login.kullanıcı_adı())
password=browser.find_element(By.XPATH,"//*[@id='password']")
password.send_keys(osm_login.password())

#giriş
grs=browser.find_element(By.XPATH,"//*[@id='login']")
grs.click()
sleep(5)

#taş alanı
ts=browser.find_element(By.XPATH,"//*[@id='balances']/div/div[1]/div/span")
ts.click()
sleep(3)

for i in range(4):
    #tas alanını kaydırma
    yatay_scroll_element = browser.find_element(By.XPATH, "//*[@id='product-category-free']/div[2]/div[1]/div/div[2]/div")

    # JavaScript ile bi elemana scrool
    tss=browser.find_element(By.XPATH,"//*[@id='product-category-adrewards']/div[1]")
    browser.execute_script("arguments[0].scrollIntoView();",tss)
    sleep(2)
    #reklama tıklama
    #rklm=browser.find_element(By.XPATH,"//*[@id='product-category-free']/div[2]/div[1]/div/div[2]/div")
    rklm=browser.find_element(By.XPATH,"//*[@id='product-category-free']/div[2]/div[1]/div")
    rklm.click()

    #reklam açma
    """rklmmm=browser.find_element(By.XPATH,"//*[@id='applixir_video']/div[1]")
    rklmmm.click()"""
    sleep(16)
    # Tıklanacak elementi bulma (Örnek olarak bir buton)

    for i in range(20):  # Örneğin 10 saniye boyunca kontrol etmeyi dene
        try:
            element = browser.find_element(By.XPATH, "//*[@id='btnClose']")
            element.click()
            break  # Buton bulunursa ve tıklanırsa döngüyü kır
        except:
            sleep(1)  # Buton bulunamazsa 1 saniye bekle ve tekrar dene

    # ActionChains'i başlatma
    actions = ActionChains(browser)

    # Belirtilen elemente tıklama işlemi
    actions.click(element).perform()

    # taş alanını kaydırma
    yatay_scroll_element = browser.find_element(By.XPATH,"//*[@id='product-category-free']/div[2]/div[1]/div/div[2]/div")


