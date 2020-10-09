from selenium import webdriver


class DriverUtils:

    driver = None
    switch = False

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver is not None and cls.switch is False:
            cls.driver.quit()
            cls.driver = None

    @classmethod
    def set_switch(cls, switch):
        cls.switch = switch
