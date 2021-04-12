

echo. ##################### TEST PATH #####################
cd /d C:\PYTHON\selenium.framework\src\test

@echo off

echo. ##################### PRUEBAS #####################


python -m pytest tst_001.py tst_002.py tst_003.py --junit-xml=../results/results.xml 





pause