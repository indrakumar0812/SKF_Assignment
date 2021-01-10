import inspect
import logging
import allure

#-------------Log generation method-------------------#
def customLogger():

    logName = inspect.stack()[1][3]
    logger = logging.getLogger(logName)
    filehandler = logging.FileHandler("../logs/Auotmationlogs.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt='%d-%m-%y %I:%M:%S %p %A')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)
    return logger

#------------Method to feed logs in allure report-------------#
def allureLogs(text):
    with allure.step(text):
        pass