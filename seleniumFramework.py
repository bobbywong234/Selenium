from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pynput import keyboard
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class selenium_preference:
    private = "browser.privatebrowsing.autostart"


def fireFox_instance_single_preference(exe_path, gecko_path, preference):
    binary = FirefoxBinary(exe_path)
    options = Options()
    options.set_preference(preference, True)
    options.binary = binary
    s = Service(gecko_path)
    return webdriver.Firefox(service=s, options=options)


def fireFox_instance_multiple_preference(exe_path, gecko_path, preferences):
    binary = FirefoxBinary(exe_path)
    options = Options()
    for preference in preferences:
        options.set_preference(preference, True)
    options.binary = binary
    s = Service(gecko_path)
    return webdriver.Firefox(service=s, options=options)


def key_press(key):
    if key == keyboard.Key.shift_r:
        return False


def refresh_frame(firefox, path, timeout=1):
    error = True
    while error:
        try:
            WebDriverWait(firefox, timeout).until(
                expected_conditions.presence_of_all_elements_located
                ((By.XPATH, path)))
            element = firefox.find_element(by=By.XPATH, value=path)
            firefox.switch_to.frame(element)
            error = False
        except (TimeoutException, NoSuchWindowException, StaleElementReferenceException, NoSuchElementException):
            firefox.switch_to.default_content()


def load_element(firefox, path, timeout):
    error = True
    while error:
        try:
            WebDriverWait(firefox, timeout).until(
                expected_conditions.presence_of_all_elements_located
                ((By.XPATH, path)))
            element_found = firefox.find_element(by=By.XPATH, value=path)
            error = False
            return element_found
        except (TimeoutException, NoSuchWindowException, StaleElementReferenceException, NoSuchElementException):
            print(path + ' element not found')


def load_children_element(parent, path, timeout):
    error = True
    while error:
        try:
            WebDriverWait(parent, timeout).until(
                expected_conditions.presence_of_all_elements_located
                ((By.XPATH, path)))
            elements_found = parent.find_element(by=By.XPATH, value=path)
            error = False
            return elements_found
        except (TimeoutException, NoSuchWindowException, StaleElementReferenceException, NoSuchElementException):
            print(path + ' child not found')


def load_children_elements(parent, path, timeout):
    error = True
    while error:
        try:
            WebDriverWait(parent, timeout).until(
                expected_conditions.presence_of_all_elements_located
                ((By.XPATH, path)))
            elements_found = parent.find_elements(by=By.XPATH, value=path)
            error = False
            return elements_found
        except (TimeoutException, NoSuchWindowException, StaleElementReferenceException, NoSuchElementException):
            print(path + ' children not found')


def load_children_elements_tag(parent, tag, timeout):
    error = True
    while error:
        try:
            WebDriverWait(parent, timeout).until(
                expected_conditions.presence_of_all_elements_located
                ((By.TAG_NAME, tag)))
            elements_found = parent.find_elements(by=By.TAG_NAME, value=tag)
            error = False
            return elements_found
        except (TimeoutException, NoSuchWindowException, StaleElementReferenceException, NoSuchElementException):
            print(tag + ' children not found')


def load_children_element_tag(parent, tag, timeout):
    error = True
    while error:
        try:
            WebDriverWait(parent, timeout).until(
                expected_conditions.presence_of_all_elements_located
                ((By.TAG_NAME, tag)))
            elements_found = parent.find_element(by=By.TAG_NAME, value=tag)
            error = False
            return elements_found
        except (TimeoutException, NoSuchWindowException, StaleElementReferenceException, NoSuchElementException):
            print(tag + ' children not found')
