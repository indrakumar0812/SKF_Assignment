import time
from Assignment.utilities.ReadProperties import ReadConfig
from Assignment.base.BaseClass import BaseClass
from Assignment.utilities.CustomLogger import allureLogs
from selenium.webdriver.support.color import Color

#----------Page Class for Select Bearing type page-----------#

class SelectBearingTypePage(BaseClass):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

#-----------page locator details---------------------#
    _bearingDropbox="//div[contains(@id,'mat-select-value-9')]" #xpath
    _listbox="//div[@role='listbox']" #xpath
    _listOptions= "//mat-option[@role='option']" #xpath
    _bearingIcon= 'bearing-icon' #className
    _designationSearchBox="//input[@placeholder='Search designation']" #xpath
    _cellDesignationValues="//mat-table[@role='grid']/mat-row/mat-cell[7]" #xpath
    _nextButton ="//button[text()='next']" #xpath

#----object to get the configuration properties-----#
    config=ReadConfig()

#--------Methods for respective action on the web elements------------#

    def clickDropDownBox(self):
        action = self.mouseHoverActions(self._bearingDropbox,"xpath")
        action.click().perform()
        allureLogs("Clicked on the drop down box")

    def getDropDownOptions(self):

        allureLogs("Verifying the ListBox")
        element = self.isDisplayed(self._listbox, 'xpath')
        if element == True:
            allureLogs("Listbox is displayed")
            element = self.getElementsList(self._listOptions,'xpath')
            return element
        else:
            allureLogs("Listbox is not displayed")
            assert False

    def selectDropDownOption(self,value):

        allureLogs(f'selecting the {value} from the drop downbox')
        element = self.isDisplayed(self._listbox, 'xpath')
        if element == True:
            allureLogs("Listbox is displayed")
            options = self.getElementsList(self._listOptions,'xpath')

            for option in options:
                if option.text == value:
                    option.click()
                    allureLogs(f'selected the {value} from the drop downbox')
                    break
                else:
                    allureLogs(f"Can't select the {value} from the drop downbox")
                    assert False
        else:
            allureLogs("Listbox is not displayed")
            assert False

    def closeDropDownOption(self):
        allureLogs("closing the dropdown box")
        action=self.mouseHoverActions(self._bearingIcon,"class")
        action.pause(2).click().perform()
        time.sleep(2)
        actual_text = self.getText(self._bearingDropbox,'xpath')
        expected_text = self.config.getDropDownBoxText()
        assert actual_text == expected_text
        allureLogs("dropdown box closed")

    def enterDesignationValue(self):
        text = self.config.getDesignationValue()
        allureLogs(f'entering the value {text} in the search bar')
        self.sendText(text,self._designationSearchBox,"xpath")
        time.sleep(4)
        cellValues = self.getElementsList(self._cellDesignationValues,"xpath")

        for value in cellValues:
            if value.text==text:
                value.click()
                allureLogs(f'cell with value {text} found and selected')
                break
            else:
                allureLogs(f'cell with value {text} could not be found')
                assert False

    def getButtonColor(self):
        #self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        allureLogs("Extracting the color of the Next button")
        buttonColor = self.getCssAttribute(self._nextButton,"xpath",self.config.getCssProperty())
        color = Color.from_string(buttonColor).hex
        allureLogs(f'Hex value of the next button is {color}')
        assert color == self.config.getHexValue()
        allureLogs("Color matched successfully")








