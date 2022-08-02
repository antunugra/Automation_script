import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class AdminTest(unittest.TestCase):
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def tc_a_add_User_valid(self):#=====================================================================================
        #----------------Login
        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() 
        time.sleep(1)

        #----------------Redirect User Management
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        #----------------Add User
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[employeeName][empName]").send_keys("Admin A")
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[userName]").send_keys("tester3")
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[password]").send_keys("tester123")
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[confirmPassword]").send_keys("tester123")
        time.sleep(1)
        browser.find_element(By.NAME, "btnSave").click()
        time.sleep(3)    
        

   
    def tc_b_add_user_invalid(self): #=====================================================================================
         #----------------Login
        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() 
        time.sleep(1)

         #----------------Redirect User Management
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

         #----------------Add User
        browser.find_element(By.NAME, "btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME, "systemUser[employeeName][empName]").send_keys("Admin @")
        time.sleep(1)
        
         #----------------Validation Error
        validation_error = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[2]/span").text
        self.assertEqual(validation_error, "Employee does not exist")
        time.sleep(2)

    def tc_d_search_user(self): #=====================================================================================
        #----------------Login
        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() 
        time.sleep(1)

        #----------------Redirect User Management
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        #----------------Search User
        browser.find_element(By.NAME, "searchSystemUser[userName]").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.NAME, "_search").click()
        time.sleep(3)

        #----------------Validate Element
        search_result = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td[2]/a").text
        self.assertEqual(search_result, 'Admin')


    def tc_e_reset(self):#=====================================================================================
        #----------------Login
        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() 
        time.sleep(1)

         #----------------Redirect User Management
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

         #----------------Search User
        browser.find_element(By.NAME, "searchSystemUser[userName]").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.NAME, "_search").click()
        time.sleep(3)
      
         #----------------Reset Search User
        browser.find_element(By.NAME, "_reset").click()
        time.sleep(3)

         #----------------Validate Reset Search
        all_user = browser.find_element(By.NAME,"frmList_ohrmListComponent").text
        
         #----------------List All User
        self.assertEqual(all_user, 'resultTable')


    def tc_f_delete_user(self): #=====================================================================================
         #----------------Login
        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        browser.find_element(By.NAME,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() 
        time.sleep(1)

         #----------------Redirect User Management
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)

         #----------------Search User
        browser.find_element(By.NAME, "searchSystemUser[userName]").send_keys("unchunch2")
        time.sleep(1)
        browser.find_element(By.NAME, "_search").click()
        time.sleep(3)

         #----------------Delete User
        browser.find_element(By.NAME, "chkSelectRow[]").click()
        time.sleep(1)
        browser.find_element(By.NAME, "btnDelete").click()
        time.sleep(1)
        browser.find_element(By.ID, "dialogDeleteBtn").click()
        time.sleep(3)

         #----------------Validate User Deleted
        browser.refresh()
        time.sleep(5)
        browser.find_element(By.NAME, "searchSystemUser[userName]").send_keys("unchunch2")
        time.sleep(1)
        browser.find_element(By.NAME, "_search").click()
        time.sleep(3)
        check_user = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td").text
        self.assertEqual(check_user, 'No Records Found')


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()