import time

from Assignment.base.BaseClass import BaseClass
from Assignment.utilities.CustomLogger import allureLogs

#----------Page Class for Bearing type page-----------#

class BearingTypePage(BaseClass):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

#-----------page locator details---------------------#

    _singleBearing='single-bearing' #className

#--------Methods for respective action on the web elements------------#

    def verifyBearingType(self):
        element = self.isDisplayed(self._singleBearing,'class')
        assert element == True
        allureLogs("Single bearing image displayed successfully")

    def clickSingleBearing(self):
        self.clickElement(self._singleBearing,'class')
        allureLogs("Clicked on the Single bearing type")

