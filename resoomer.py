from selenium import webdriver

textToSumrize = [
    "from your description it appears that you may have anterior knee pain which sometimes presents as pain at the back of the knee. the second possibility is that you have over done your exercise and hamstrings are sore and the lower end of the knee cap is inflamed. either way you should rest and ice the area of pain and give it time. i suggest you add nsaids (nonsteroidal anti-inflammatory drugs) for a week for an additional anti-inflammatory action. for further information consult an orthopaedician and traumatologist online --> <link>",    
    "depression anxiety restlessness and panic attacks are best respond to a combination of a selective serotonin reuptake inhibitors (ssris) and benzodiazepines. mirtazapine is not the most efficient ant depressant and it is not a true ssri as fluoxetine paroxetine citalopram and sertraline are. i recommend 20 to 40mg of paroxetine (slowly titrated up from 10mg) and 1mg of either clonazepam or ativan (lorazepam) every 8 hours as needed for anxiety. glaucoma precludes use of any anticholinergics such as hydroxyzine or benadryl (diphenhydramine). ssris are also at times likely to make glaucoma worse but a preliminary trial is always worth it. revert back to a psychiatrist online for further help --> <link>"
    ]

sumrizedText = []
options = webdriver.ChromeOptions()
options.add_argument("start-maximized") # open Browser in maximized mode
options.add_argument("disable-infobars") # disabling infobars
options.add_argument("--disable-extensions") # disabling extensions
options.add_argument("--disable-gpu") # applicable to windows os only
options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems
options.add_argument("--no-sandbox") # Bypass OS security model
driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe',chrome_options=options)

for idx in range(len(textToSumrize)):

    print("Phase : ", idx)
    driver.get('https://resoomer.com/en/')    

    textArea = driver.find_element_by_css_selector('#contentText')
    textArea.clear()
    textArea.send_keys(textToSumrize[idx])

    resoomerBtn = driver.find_element_by_css_selector("#btnSendText_V2")
    resoomerBtn.submit()

    outputText = driver.find_element_by_css_selector("#conteneurTextAuto")    
    sumrizedText.append(outputText.text)    

print("\n",sumrizedText)