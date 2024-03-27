from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.common.keys import Keys
import json

class TestMarineTrafficLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
    
    def vessels_infos(self):
        shipids = ['714556', '371681', '5630138', '371668', '371584', '372813', '429068', '400773', '442329']
        for _id in shipids:
            dashboard_url = 'https://www.marinetraffic.com/en/ais/details/ships/shipid:'+str(_id)
            self.driver.get(dashboard_url)

            name_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="vesselDetails_generalSection"]/div[2]/table/tbody/tr[1]/td'))
            )
            name = name_element.text

            imo_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="vesselDetails_generalSection"]/div[2]/table/tbody/tr[3]/td'))
            )
            imo = imo_element.text

            mmsi_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="vesselDetails_generalSection"]/div[2]/table/tbody/tr[4]/td'))
            )
            mmsi = mmsi_element.text

            speed_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="vesselDetails_aisInfoSection"]/div[1]/table/tbody/tr[5]/td'))
            )
            speed = speed_element.text

            course_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="vesselDetails_aisInfoSection"]/div[1]/table/tbody/tr[6]/td'))
            )
            course = course_element.text

            data = {
                "name": name,
                "imo": imo,
                "mmsi": mmsi,
                "speed": speed,
                "course": course
            }
            json_str = json.dumps(data, indent = 3)
            print(json_str)

    def test_login(self):
        email = 'xxx' # write your email
        password = 'xxx' # write your password
        url = 'https://www.marinetraffic.com/en/users/login'
        self.driver.get(url)

        agree_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "css-1yp8yiu"))
        )
        agree_button.click()

        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "email"))
        )
        email_field.send_keys(email)

        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password_field.send_keys(password)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login_form_submit"))
        )
        login_button.click()
        self.vessels_infos()
    
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()