import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PlaceOrderUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://127.0.0.1:8000"

    def test_placeOrder(self):
        driver = self.driver

        driver.get(f"{self.base_url}/registration/login/")
        driver.find_element(By.NAME, "username").send_keys("testuser")
        driver.find_element(By.NAME, "password").send_keys("testpass123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        WebDriverWait(driver, 10).until(
            EC.url_changes(f"{self.base_url}/registration/login/")
        )

        driver.get(f"{self.base_url}/1/")

        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Add to cart']"))
        )
        add_to_cart_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/cart/")
        )

        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/orders/create/')]"))
        )
        checkout_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "first_name"))
        ).send_keys("Nate")

        driver.find_element(By.NAME, "last_name").send_keys("Brown")
        driver.find_element(By.NAME, "email").send_keys("testuser@gmail.com")
        driver.find_element(By.NAME, "address").send_keys("123 Maverick Way")
        driver.find_element(By.NAME, "postal_code").send_keys("68182")
        driver.find_element(By.NAME, "city").send_keys("Omaha")

        submit_order_button = driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_order_button.click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Complete Your Payment')]"))
        )

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "name"))
        ).send_keys("John Doe")

        driver.find_element(By.ID, "card-number").send_keys("4111222233334444")
        driver.find_element(By.ID, "expiry").send_keys("12/30")
        driver.find_element(By.ID, "cvv").send_keys("123")
        driver.find_element(By.ID, "billing-zip").send_keys("68182")

        pay_button = driver.find_element(By.CSS_SELECTOR, ".pay-btn")
        pay_button.click()

        self.assertIn("successfully", driver.page_source.lower())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()