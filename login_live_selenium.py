try:
    elem = driver.find_element_by_name('loginfmt')
    elem.clear()
    elem.send_keys("your_email_id") # add your login email id
    elem.send_keys(Keys.RETURN)
wait_for(5)
elem1 = driver.find_element_by_name('passwd')
    elem1.clear()
    elem1.send_keys("your_password") # add your password
elem1.send_keys(Keys.ENTER)
    wait_for(7)
 
except Exception as e:
    print(e)
    wait_for(4)
