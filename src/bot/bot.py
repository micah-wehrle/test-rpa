from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement

from .setup_driver import create_chromium_driver

class Bot:
  def __init__(self):
    self.driver = create_chromium_driver()

    self.page_is_open = False
  
  def open_new_browser(self, url):
    if self.page_is_open:
      raise Exception("Already have webpage open. Must close before opening new page.")
    else:
      self.driver.get(url)
      self.page_is_open = True
  
  def close_page(self):
    if not self.page_is_open:
      raise Exception("No page open to close.")
    else:
      self.driver.quit()
      self.page_is_open = False
  
  def _find_element(self, search_type, locator) -> WebElement:

    # Setup search delay for up to 500 ms
    wait = WebDriverWait(driver=self.driver, timeout=0.5, poll_frequency=0.05)

    try:
      # Attempt to find element based on given search_type and locator
      element = wait.until(lambda _ : self.driver.find_element(search_type, locator))

      return element
    except TimeoutException:
      raise Exception(f"Unable to find specified element by {search_type} as {locator}")
    
  def find_id(self, id) -> WebElement:
    element = self._find_element(search_type=By.ID, locator=id)
    return element
  
  def find_class(self, class_name) -> WebElement:
    element = self._find_element(search_type=By.CLASS_NAME, locator=class_name)
    return element
  
  def find_xpath(self, xpath) -> WebElement:
    element = self._find_element(search_type=By.XPATH, locator=xpath)
    return element

  def get_driver(self):
    return self.driver

  
