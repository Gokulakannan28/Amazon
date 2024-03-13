import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.implicitly_wait(30)
class Amazon:
    def openbrowser(self):
        driver.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=155259815513&hvpone=&hvptwo=&hvadid=674842289437&hvpos=&hvnetw=g&hvrand=11343757163317254957&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9148781&hvtargid=kwd-10573980&hydadcr=14453_2316415&gad_source=1")
        driver.maximize_window()
    def login(self):
        try:
            driver.find_element(By.XPATH, "//div[@id='nav-signin-tooltip']/a/span").click()
            driver.find_element(By.ID, "ap_email").send_keys("kgokul192@gmail.com")
            driver.find_element(By.ID, "continue").click()
            driver.find_element(By.ID, "ap_password").send_keys("Gokul@1994")
            driver.find_element(By.ID, "signInSubmit").click()
        except:
            driver.close()
            print("Page was not available")

    def searchbar(self):
        driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Redmi 12 5G Moonstone")
        driver.find_element(By.ID, "nav-search-submit-button").click()
        driver.execute_script("window.scrollBy(0,300);")
        driver.find_element(By.LINK_TEXT, "Redmi 12 5G Moonstone Silver 6GB RAM 128GB ROM").click()

    def addtocart(self):
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.execute_script("window.scrollBy(0,400);")
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div[3]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div/div[36]/div[1]/span/span/span/input").click()
        driver.find_element(By.XPATH, "//*[@id='nav-cart']").click()
    def Buy(self):
        driver.find_element(By.XPATH, "//*[@id='sc-buy-box-ptc-button']/span/input").click()
        driver.find_element(By.XPATH, "//*[@id='address-list']/div/div[1]/div/fieldset[1]/div[2]/span/div/label/span/span[2]").click()
        driver.find_element(By.XPATH, "//*[@id='shipToThisAddressButton']/span/input").click()
        driver.execute_script("window.scrollBy(0,500);")
        driver.find_element(By.XPATH, "//*[@id='pp-OfSmQf-402']/div/div/div/div/div[2]").click()
        driver.find_element(By.XPATH, "//*[@id='pp-OfSmQf-405']/span/input").click()
        time.sleep(10)


obj = Amazon()
obj.openbrowser()
obj.login()
obj.searchbar()
obj.addtocart()
obj.Buy()
