import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://127.0.0.1:8000"

    def test_loginGood(self):
        driver = self.driver

        driver.get(f"{self.base_url}/registration/login/")

        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        username_field.send_keys("testuser")
        password_field.send_keys("testpass123")
        login_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_changes(f"{self.base_url}/registration/login/")
        )

        self.assertIn("Profile Information", driver.page_source)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()