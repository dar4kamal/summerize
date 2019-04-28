from selenium import webdriver

originalText = input("Enter Full Text: ")

driver = webdriver.Chrome()
driver.get('https://resoomer.com/en/')

textArea = driver.find_element_by_css_selector('#contentText')
textArea.send_keys(originalText)

resoomerBtn = driver.find_element_by_css_selector("#btnSendText_V2")
resoomerBtn.submit()

outputText = driver.find_element_by_css_selector("#conteneurTextAuto")
print(outputText.text)