from selenium import webdriver
driver = webdriver.PhantomJS()

driver.set_window_size(1120, 550)
driver.implicitly_wait(30)
driver.get("https://browse-query-editor-na.aka.amazon.com/?browseNodeFilter=category-node-merchant-facing&catalogAttributes=title&marketplaceId=1&pageSize=5&retailAsins=N&showImages=Y&useSuggestedBrowseNode=N&userQuery=%5Bpackage_weight.pounds%3A-10%5D&variationParentOnly=N&websiteSearchable=N")
print(driver.title)
if(driver.find_element_by_xpath('//*[@id="redux-app"]/div/div[3]/div/div/div/div/span').is_displayed):
    print(driver.find_element_by_xpath('//*[@id="redux-app"]/div/div[3]/div/div/div/div/span').get_attribute('value'))
    elements = driver.find_element_by_xpath('//*[@id="redux-app"]/div/div[5]/table/tbody/tr[1]/td[4]').get_property('name')
    print(elements)
    elements = driver.find_element_by_xpath('//*[@id="redux-app"]/div/div[5]/table/tbody/tr[1]/td[4]').get_attribute('name')
    print(elements)

#for s in size:
 #   asin= driver.find_element_by_xpath("//tbody//tr["+s+"]/td[3]/a[1]").get_property('name')
#print(asin)
driver.quit()