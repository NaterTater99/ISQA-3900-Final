import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ViewMyOrdersUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://127.0.0.1:8000"

    def test_viewMyOrders(self):
        driver = self.driver

        driver.get(f"{self.base_url}/registration/login/")
        driver.find_element(By.NAME, "username").send_keys("testuser")
        driver.find_element(By.NAME, "password").send_keys("testpass123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        WebDriverWait(driver, 10).until(
            EC.url_changes(f"{self.base_url}/registration/login/")
        )

        view_orders_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'View My Orders')]"))
        )
        view_orders_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/orders/my-orders/")
        )

        self.assertIn("My Order History", driver.page_source)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()