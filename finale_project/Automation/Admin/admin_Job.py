import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class AdminTest(unittest.TestCase):
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def tc_a_add_job_tittle(self):#=====================================================================================
        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() 
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(2)
        #----------------Hover to Job Title
        job = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/a")
        job_title = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[1]/a")
        pay_grade = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[2]/a")
        employ_stat = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[3]/a")
        job_cat = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[4]/a")
        work_shift = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[5]/a")

        actions = ActionChains(browser)

        #----------------Click Job Title
        actions.move_to_element(job).move_to_element(job_title).click().perform()
        time.sleep(3)

        #----------------Validate
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewJobTitleList"
        self.assertEqual(expected_current_url, browser.current_url)

        #----------------Add Job Titles
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME, "jobTitle[jobTitle]").send_keys("Kang Rumput3")
        time.sleep(1)
        browser.find_element(By.NAME, "jobTitle[jobDescription]").send_keys("Sukanya bebersih rumput, bebersih taman, siramin tanaman, pokoknya bersih pangkal kaya1")
        time.sleep(1)
        browser.find_element(By.NAME, "jobTitle[note]").send_keys("ini perlu buat memperindah taman dan kebun1")
        time.sleep(1)
        browser.find_element(By.NAME, "btnSave").click()
        time.sleep(1)

    def tc_b_delete_job_tittle(self): #=====================================================================================
        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() 
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(2)

        #----------------Hover to Job Title
        job = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/a")
        job_title = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[1]/a")

        actions = ActionChains(browser)

        #----------------Click Job Title
        actions.move_to_element(job).move_to_element(job_title).click().perform()
        time.sleep(3)
        
        #----------------Validate
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewJobTitleList"
        self.assertEqual(expected_current_url, browser.current_url)

        #----------------Delete Job Title
        browser.find_element(By.NAME, "chkSelectRow[]").click()
        time.sleep(1)
        browser.find_element(By.NAME, "btnDelete").click()
        time.sleep(1)
        browser.find_element(By.ID, "dialogDeleteBtn").click()
        time.sleep(1)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()