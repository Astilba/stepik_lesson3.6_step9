import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_exists(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    time.sleep(15)
    assert len(browser.find_elements_by_class_name('btn-add-to-basket')) != 0, 'The button does not exist.'
