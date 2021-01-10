import pytest
from Assignment.pages.BearingTypePage import BearingTypePage
from Assignment.pages.HomePage import HomeSKFPage
from Assignment.pages.TypeAndArrangementPage import SelectBearingTypePage
from Assignment.utilities.CustomLogger import customLogger

@pytest.mark.usefixtures('setup')
class Test_002_ButtonColor():

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.dp = SelectBearingTypePage(self.driver)
        self.hp = HomeSKFPage(self.driver)
        self.bp = BearingTypePage(self.driver)
        self.cl = customLogger()

    def test_NextButtonColor(self):
        self.cl.info("--------------------Test_002_ButtonColor------------------------------")
        self.hp.clickAcceptButton()
        self.hp.clickBearingImage()
        self.hp.verifyTitle()
        self.bp.verifyBearingType()
        self.bp.clickSingleBearing()
        self.cl.info("--------------------Clicking on drop downbox---------------------------")
        self.dp.clickDropDownBox()
        self.cl.info("--------------------Selecting option from drop downbox------------------")
        self.dp.selectDropDownOption("Deep groove ball bearing")
        self.cl.info("--------------------Entering value in designation search bar------------")
        self.dp.enterDesignationValue()
        self.cl.info("--------------------Fetching Next Button Color--------------------------")
        self.dp.getButtonColor()
        self.cl.info("--------------------Next Button Color Verification successful------------")


