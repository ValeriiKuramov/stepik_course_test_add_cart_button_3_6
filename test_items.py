from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_add_to_cart_button_exists(browser):
    # test verifies that the product page on the website contains the "add to cart" button
    browser.get(link)
    # an indicator of the presence or absence of a button
    contain_an_add_to_cart_button = True
    try:
        # we are looking for and for reliability we press the button
        button_add_cart = (WebDriverWait(browser, 20)
                           .until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"))))
        button_add_cart.click()
    except:
        # in case of an error, we assume that the button was not found
        contain_an_add_to_cart_button = False
    assert contain_an_add_to_cart_button, "The site does not contain the 'add to cart' button"