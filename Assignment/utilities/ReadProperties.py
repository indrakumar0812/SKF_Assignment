import configparser

class ReadConfig:

#-----Reading the configuration file-------------#
    config = configparser.RawConfigParser()
    config.read("../configurationFiles/config.ini")

#-----Methods to fetch the value from configurations file---------#
    def getUrl(self):
        url = self.config.get("Website","url")
        return url

    def getTitle(self):
        title = self.config.get("HomePageTitle","title")
        return title

    def getDropDownBoxText(self):
        dropboxText = self.config.get("DropBoxText","text")
        return dropboxText

    def getDesignationValue(self):
        value=self.config.get("DesignationValue","value")
        return value

    def getCssProperty(self):
        cssProperty=self.config.get("CssProperties","property")
        return cssProperty

    def getHexValue(self):
        color=self.config.get("CssProperties","color")
        return color


