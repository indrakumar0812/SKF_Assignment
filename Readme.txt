Prerequisite:
1) Python 3.9 should be installed
2) Chrome and firefox browser should be installed in system

Steps to run the tests:
1) Navigate to the 'tests' folder
2) Open the terminal in the 'tests folder'
3) In the terminal type the following command
	py.test -s -v --alluredir reports
4) Once test is completed run the following command
	allure serve reports
5) If the test has to be run in the 'firefox' browser then run the command
	py.test -s -v --browser=firefox --alluredir reports
