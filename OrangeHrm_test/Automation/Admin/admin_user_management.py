import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class AdminTest(unittest.TestCase):
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_tambah_user_valid(self):
        #Login-----------------------
        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() 
        time.sleep(1)

        #Menuju halaman user----------
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        #Tambah user------------------
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[employeeName][empName]").send_keys("Ananya Dash")
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[userName]").send_keys("kintuna")
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[password]").send_keys("kinul123")
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[confirmPassword]").send_keys("kinul123")
        time.sleep(1)
        browser.find_element(By.NAME, "btnSave").click()
        time.sleep(1)
        browser.find_element(By.NAME, "searchSystemUser[userName]").send_keys("kintuna")
        time.sleep(1)
        browser.find_element(By.NAME, "_search").click()
        time.sleep(3)
        search_result = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td[2]/a").text
        self.assertEqual(search_result, 'kintuna')


    def test_b_tambah_user_invalid(self): 
        #Login-----------------------
        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() 
        time.sleep(1)

        #Menuju Halaman User---------
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        #Tambah User-----------------
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[employeeName][empName]").send_keys("kenuls")
        time.sleep(1)
        
        #Validasi Error--------------
        validation_error = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[2]/span").text
        self.assertEqual(validation_error, "Employee does not exist")
        time.sleep(2)

    def test_d_mencari_user(self):
        #Login----------------------
        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() 
        time.sleep(1)

        #Menuju Halaman User-------
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        #Mencari User--------------
        browser.find_element(By.NAME, "searchSystemUser[userName]").send_keys("kintuna")
        time.sleep(1)
        browser.find_element(By.NAME, "_search").click()
        time.sleep(3)

        #Validasi Elemen-----------
        search_result = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td[2]/a").text
        self.assertEqual(search_result, 'kintuna')

    def test_e_mereset_kolom(self):
        #Login---------------------
        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() 
        time.sleep(1)

        #Menuju Halaman User-------
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        #Mencari User--------------
        browser.find_element(By.NAME, "searchSystemUser[userName]").send_keys("adminkenul")
        time.sleep(1)
        browser.find_element(By.NAME, "_search").click()
        time.sleep(3)

        #Reset Mencari User--------
        browser.find_element(By.NAME, "_reset").click()
        time.sleep(3)
        
        #Validasi Reset User------
        all_user = browser.find_element(By.NAME,"frmList_ohrmListComponent").text
        self.assertEqual(all_user, 'resultTable')

    
    def test_f_menghapus_data_user(self):
        #Login--------------------
        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() 
        time.sleep(1)

        #Menuju Halaman User-------
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        #Mencari User-------------
        browser.find_element(By.NAME, "searchSystemUser[userName]").send_keys("kintuna")
        time.sleep(1)
        browser.find_element(By.NAME, "_search").click()
        time.sleep(3)

        #Menghapus User-----------
        browser.find_element(By.NAME, "chkSelectRow[]").click()
        time.sleep(1)
        browser.find_element(By.NAME, "btnDelete").click()
        time.sleep(1)
        browser.find_element(By.ID, "dialogDeleteBtn").click()
        time.sleep(3)

        #Validasi Hapus User------
        browser.refresh()
        time.sleep(5)
        browser.find_element(By.NAME, "searchSystemUser[userName]").send_keys("kintuna")
        time.sleep(1)
        browser.find_element(By.NAME, "_search").click()
        time.sleep(3)
        check_user = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td").text
        self.assertEqual(check_user, 'No Records Found')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()