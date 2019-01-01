import time

from webdriver_wrapper import WebDriverWrapper


def lambda_handler(*args, **kwargs):
    driver = WebDriverWrapper()

    driver.get_url('https://www.google.es/')

    time.sleep(0.5)
    print("--------------------------")

    print("--------------------------")

    driver.close()
