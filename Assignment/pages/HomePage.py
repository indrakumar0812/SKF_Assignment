import time

from Assignment.base.BaseClass import BaseClass
from Assignment.utilities.CustomLogger import allureLogs
from Assignment.utilities.ReadProperties import ReadConfig

#----------Page Class for Home page-----------#

class HomeSKFPage(BaseClass):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

# -----------page locator details---------------------#
    _RollBearingImage='//*[@class="option-image"]' #xpath
    _AcceptButton = "//button[@type='button']" #xpath

    config= ReadConfig() #object to get the configuration properties

# --------Methods for respective action on the web elements------------#

    def clickAcceptButton(self):
        self.clickElement(self._AcceptButton,'xpath')
        allureLogs("clicked on accept & continue button")

    def clickBearingImage(self):
        self.clickElement(self._RollBearingImage,'xpath')
        allureLogs("Clicked on the Rolling Bearing Image")

    def verifyTitle(self):
        actual_title = self.getTitle()
        expected_title = self.config.getTitle()
        assert actual_title == expected_title
        allureLogs("Home page verified successfully")




