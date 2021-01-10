import collections
import pytest
from Assignment.utilities.CustomLogger import customLogger
from Assignment.pages.HomePage import HomeSKFPage
from Assignment.pages.BearingTypePage import BearingTypePage
from Assignment.pages.TypeAndArrangementPage import SelectBearingTypePage
from Assignment.utilities.ExcelUtils import readExcelData

@pytest.mark.usefixtures("setup")
class Test_001_DropDown:

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.hp = HomeSKFPage(self.driver)
        self.bp = BearingTypePage(self.driver)
        self.dp = SelectBearingTypePage(self.driver)
        self.cl = customLogger()
        self.el = readExcelData()

    def test_HomePageTitle(self):
        self.cl.info("--------------------Test_001_DropDown------------------------------")
        self.cl.info("--------------------Clicking on Accept & Continue button------")
        self.hp.clickAcceptButton()
        self.cl.info("--------------------Verifying Home Page Title-----------------")
        self.hp.clickBearingImage()
        self.hp.verifyTitle()
        self.cl.info("--------------------Home Page Title Verified Succesfully-------")

    def test_SelectSingleBearing(self):
        self.cl.info("--------------------Verifying Single Bearing type---------------")
        self.bp.verifyBearingType()
        self.bp.clickSingleBearing()
        self.cl.info("--------------------Single Bearing type selected----------------")

    def test_GetDropBoxValues(self):
        self.cl.info("--------------------Getting all Bearing type options-------------")
        self.dp.clickDropDownBox()
        testList=[]
        bearingTypes = self.dp.getDropDownOptions()

        for bearing in bearingTypes:
            testList.append(bearing.text)

        assert collections.Counter(testList)==collections.Counter(self.el)
        self.cl.info("---Successfully verified the options in the bearing type dropbox---")

    def test_closeDropDownBox(self):
        self.dp.closeDropDownOption()
        self.cl.info("--------------------Drop down Listbox closed-------------")

