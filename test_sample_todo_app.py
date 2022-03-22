from selenium import webdriver
from selenium.wedriver.common.keys import Keys
import os
import json

url = os.getenv("LT_HUB_URL")
capabilities = {
		"build" : "LT_BUILD_NAME",
		"name" : "QUICK TEST",
		"platform" : "Windows 11",
		"browserName" : "Chrome",
		"version" : "100.0",
		"resolution" : "1280x800",
		"tunnel" : True
	}

driver = webdriver.Remote(
    desired_capabilities= capabilities,
    command_executor= url
)
driver.get("http://localhost:8081")
driver.find_elemnt_by_name("li3").click()

textbox = driver.find_elemnt_by_name("sampletodotxt")
textbox.send_keys("Testing")
driver.find_elemnt_by_id("addbutton").click()
assert "No results found." not in driver.page_source
driver.execute_script("lambda-status=passed")
driver.quit()
