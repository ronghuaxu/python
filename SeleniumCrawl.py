# coding = utf-8
from selenium import webdriver
driver = webdriver.Chrome("/Users/huazi/Downloads/tools/chromedriver")

# driver.get('http://radar.kuaibo.com')
driver.get('http://www.cnblogs.com/cate/java/')
for i in range(2):
    if(i == 0):
        continue
    temp = driver.find_element_by_xpath('//*[@id="post_list"]/div[' + str(i) + ']/div[2]/h3/a')
    now_handle = driver.current_window_handle
    print now_handle
    temp.click()
    driver.implicitly_wait(3000)
    all_handles = driver.window_handles  
    print all_handles
    for handle in all_handles:
	    if handle != now_handle:
	        driver.switch_to_window(handle)
	        driver.implicitly_wait(3000)
	        content=driver.find_element_by_xpath('//*[@id="topics"]').text
	        print content
	        driver.implicitly_wait(30)
	        driver.switch_to_window(now_handle) 
    print temp.text
    

print driver.title

driver.quit()
