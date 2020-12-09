from selenium import webdriver


class DriverUtils:

    __driver = None
    __switch = False

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(10)
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None and cls.__switch is False:
            cls.__driver.quit()
            cls.__driver = None

    @classmethod
    def set_switch(cls, switch):
        cls.__switch = switch
