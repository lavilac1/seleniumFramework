

echo. ##################### TEST PATH #####################
cd /d C:\PYTHON\selenium.framework\src\test

@echo off

echo. ##################### PRUEBAS #####################


python -m pytest tst_018.py --alluredir ..\allure-results
python -m pytest tst_015.py --alluredir ..\allure-results
python -m pytest tst_014.py --alluredir ..\allure-results

pause