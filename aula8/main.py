import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def press(self, value):
    WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, f"button[value='{value}']")
        )
    ).click()

def get_display(self):
    return WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "display")
        )
    ).text.strip()

def clear_calc(self):
    self.driver.find_element(By.ID, "clear_button").click()

class DuckCalculatorTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("https://duckduckgo.com/?q=calculator")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "display"))
        )

    def press(self, value):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    f"button[value='{value}']"
                )
            )
        ).click()

    def get_display(self):
        return self.driver.find_element(
            By.ID,
            "display"
        ).text.strip()

    def clear_calc(self):
        try:
            self.press("C")
        except:
            pass

    # EXERCÍCIO A
    def test_a_soma(self):
        self.clear_calc()

        self.press("1")
        self.press("5")

        self.press("+")

        self.press("7")

        self.press("=")

        resultado = self.get_display()

        self.assertEqual(resultado, "22")

    # EXERCÍCIO B
    def test_b_multiplica_e_divide(self):
        self.clear_calc()

        self.press("8")
        self.press("×")
        self.press("5")
        self.press("=")

        self.press("÷")
        self.press("1")
        self.press("0")
        self.press("=")

        resultado = self.get_display()

        self.assertEqual(resultado, "4")

    # EXERCÍCIO C
    def test_c_duas_operacoes(self):
        self.clear_calc()

        self.press("2")
        self.press("0")

        self.press("-")

        self.press("5")

        self.press("=")

        self.assertEqual(self.get_display(), "15")

        self.press("+")

        self.press("8")

        self.press("=")

        self.assertEqual(self.get_display(), "23")

    # EXERCÍCIO D
    def test_d_historico(self):
        self.clear_calc()

        # 9 + 1 = 10
        self.press("9")
        self.press("+")
        self.press("1")
        self.press("=")

        self.assertEqual(self.get_display(), "10")

        # *2 = 20
        self.press("×")
        self.press("2")
        self.press("=")

        self.assertEqual(self.get_display(), "20")

        # -5 = 15
        self.press("-")
        self.press("5")
        self.press("=")

        self.assertEqual(self.get_display(), "15")

        history_text = self.driver.page_source

        self.assertIn("9", history_text)
        self.assertIn("1", history_text)
        self.assertIn("2", history_text)
        self.assertIn("5", history_text)


if __name__ == "__main__":
    unittest.main()