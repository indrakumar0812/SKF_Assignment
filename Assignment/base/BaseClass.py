import time

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from Assignment.utilities.CustomLogger import customLogger

class BaseClass:

    #----Creating object of logger class----#
    logs = customLogger()

    def __init__(self,driver):
        self.driver=driver

    def waitForElement(self,locatorValue,locatorType):
        locatorType=locatorType.lower()
        ele=None
        self.wait = WebDriverWait(self.driver,20,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
                                                                                    ElementNotVisibleException,
                                                                                    ElementNotSelectableException])
        if locatorType == "id":
            ele = self.wait.until(lambda x:x.find_element_by_id(locatorValue))
            return ele

        elif locatorType == "css":
            ele = self.wait.until(lambda x:x.find_element_by_css(locatorValue))
            return ele

        elif locatorType == "xpath":
            ele = self.wait.until(lambda x:x.find_element_by_xpath(locatorValue))
            return ele

        elif locatorType == "class":
            ele = self.wait.until(lambda x:x.find_element_by_class_name(locatorValue))
            return ele

        else:
            self.logs.info("Locator Value" +locatorValue+ "not found")

    def waitForElements(self, locatorValue, locatorType):

        if locatorType == "id":
            ele = self.wait.until(lambda x:x.find_elements_by_id(locatorValue))
            return ele

        elif locatorType == "css":
            ele = self.wait.until(lambda x:x.find_elements_by_css(locatorValue))
            return ele

        elif locatorType == "xpath":
            ele = self.wait.until(lambda x:x.find_elements_by_xpath(locatorValue))
            return ele

        elif locatorType == "class":
            ele = self.wait.until(lambda x:x.find_elements_by_class_name(locatorValue))
            return ele

        else:
            self.logs.info("Locator Value" +locatorValue+ "not found")

    #-------------Method to perform click on an element--------------#
    def clickElement(self,locatorValue,locatorType='id'):
        element =None
        try:
            locatorType = locatorType.lower()
            element=self.waitForElement(locatorValue,locatorType)
            element.click()
            self.logs.info("Element clicked with the locator type:" + locatorType + " and with the locator value:" + locatorValue)

        except:
            self.logs.info("Unable to click on the element with the locator type:" +locatorType+ " and with the locator value:" + locatorValue)
            self.getScreenshot(locatorType)
            assert False

    # -------------Method to verify if element is displayed--------------#
    def isDisplayed(self,locatorValue,locatorType='id'):
        element=None
        try:
            locatorType=locatorType.lower()
            element=self.waitForElement(locatorValue,locatorType)
            element.is_displayed()
            self.logs.info("Element with the locator type:" + locatorType + " and with the locator value:" + locatorValue + "is displayed")
            return True

        except:
            self.logs.info("Element with the locator type:" + locatorType + " and with the locator value:" + locatorValue + "is not displayed")
            self.getScreenshot(locatorType)
            return False

    # -------------Method to retrieve the title of a webpage--------------#
    def getTitle(self):
        title = self.driver.title
        return title

    # -------------Method to retrieve list of elements--------------#
    def getElementsList(self,locatorValue,locatorType):
        element=None
        try:
            locatorType=locatorType.lower()
            elements=self.waitForElements(locatorValue,locatorType)
            self.logs.info("All Elements with the locator type:" + locatorType + " and with the locator value:" + locatorValue + "has been retrieved")
            return elements

        except:
            self.logs.info("Elements with the locator type:" + locatorType + " and with the locator value:" + locatorValue + "couldn't be retrieved")
            self.getScreenshot(locatorType)
            assert False

    # -------------Method to perform mouse hover action--------------#
    def mouseHoverActions(self,locatorValue,locatorType):
        element=None
        try:
            locatorType=locatorType.lower()
            element=self.waitForElement(locatorValue,locatorType)
            action= ActionChains(self.driver)
            action.move_to_element(element)
            self.logs.info("Mouseover Action on locator type:" + locatorType + " and with the locator value:" + locatorValue + "is successful")
            return action

        except:
            self.logs.info("Mouseover Action on locator type:" + locatorType + " and with the locator value:" + locatorValue + "is unsuccessful")
            self.getScreenshot(locatorType)
            assert False

    # -------------Method to retrieve text from an element--------------#
    def getText(self,locatorValue,locatorType):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            text = element.text
            self.logs.info("Text of the element on locator type:" + locatorType + " and with the locator value:" + locatorValue + "is extracted")
            return text
        except:
            self.logs.info("Text of the element on locator type:" + locatorType + " and with the locator value:" + locatorValue + "couldn't be extracted")
            self.getScreenshot(locatorType)
            assert False

    # -------------Method to enter a value to an element--------------#
    def sendText(self,text,locatorValue,locatorType='id'):
        element= None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue,locatorType)
            element.send_keys(text)
            self.logs.info("Send text on Element with the locator type:" +locatorType+ " and with the locator value:" +locatorValue)
        except:
            self.logs.info("Unable to send text on Element with the locator type:" +locatorType+ " and with the locator value:" +locatorValue)
            self.getScreenshot(locatorType)
            assert False

    # -------------Method to retrieve CSS property an element--------------#
    def getCssAttribute(self,locatorValue,locatorType,property):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            cssValue = element.value_of_css_property(property)
            self.logs.info("Css Attribute of the Element with the locator type:" + locatorType + " and with the locator value:" + locatorValue + "is retrieved successfully")
            return cssValue
        except:
            self.logs.info("Css Attribute of the Element with the locator type:" + locatorType + " and with the locator value:" + locatorValue + "couldn't be retrieved")
            self.getScreenshot(locatorType)
            assert False

    # -------------Method to capture screenshot--------------#
    def getScreenshot(self,screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName

        try:
            self.driver.get_screenshot_as_file(screenshotPath)
            self.logs.info("screenshot saved to the path:" +screenshotPath)

        except:
            self.logs.info("Unable to save the screenshot to the path:" + screenshotPath)
