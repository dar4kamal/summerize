from selenium import webdriver

originalText = input("Enter Full Text: ")

textToSumrize = [
    "depression anxiety restlessness and panic attacks are best respond to a combination of a selective serotonin reuptake inhibitors (ssris) and benzodiazepines. mirtazapine is not the most efficient ant depressant and it is not a true ssri as fluoxetine paroxetine citalopram and sertraline are. i recommend 20 to 40mg of paroxetine (slowly titrated up from 10mg) and 1mg of either clonazepam or ativan (lorazepam) every 8 hours as needed for anxiety. glaucoma precludes use of any anticholinergics such as hydroxyzine or benadryl (diphenhydramine). ssris are also at times likely to make glaucoma worse but a preliminary trial is always worth it. revert back to a psychiatrist online for further help",
    "depression anxiety restlessness and panic attacks are best respond to a combination of a selective serotonin reuptake inhibitors (ssris) and benzodiazepines. mirtazapine is not the most efficient ant depressant and it is not a true ssri as fluoxetine paroxetine citalopram and sertraline are. i recommend 20 to 40mg of paroxetine (slowly titrated up from 10mg) and 1mg of either clonazepam or ativan (lorazepam) every 8 hours as needed for anxiety. glaucoma precludes use of any anticholinergics such as hydroxyzine or benadryl (diphenhydramine). ssris are also at times likely to make glaucoma worse but a preliminary trial is always worth it. revert back to a psychiatrist online for further help"
    ]

sumrizedText = []

driver = webdriver.Chrome()
driver.get('https://resoomer.com/en/')

for text in textToSumrize:
    print("Phase : ", textToSumrize.index(text))
    textArea = driver.find_element_by_css_selector('#contentText')
    textArea.send_keys(originalText)

    resoomerBtn = driver.find_element_by_css_selector("#btnSendText_V2")
    resoomerBtn.submit()

    outputText = driver.find_element_by_css_selector("#conteneurTextAuto")
    sumrizedText.append(outputText.text)

    deleteTextBtn = driver.find_element_by_class_name("formatResoomer")
    deleteTextBtn.submit()    

print("\n",sumrizedText)