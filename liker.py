from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import selenium.common.exceptions

driver = webdriver.Chrome("./chromedriver")

number = 4

username = "username"
password = "password"


def like_pic():
    time.sleep(2)
    like = driver.find_element_by_class_name('fr66n')
    like.find_element_by_tag_name('button').click()
    # soup = bs(like.get_attribute('innerHTML'),'html.parser')
    # if(soup.find('svg')['aria-label'] == 'Like'):
    #     like.click()
    # time.sleep(2)

def next_picture():
    time.sleep(2)
    try:
        nex = driver.find_element_by_class_name("coreSpriteRightPaginationArrow")
        time.sleep(1)
        return nex
    except selenium.common.exceptions.NoSuchElementException:
        return 0

def continue_liking():
    count = 0
    while(True):
        next_el = next_picture()
 
        # if next button is there then
        if next_el != False and count <= 23:
 
            # click the next button
            next_el.click()
            time.sleep(2)
 
            # like the picture
            like_pic()
            time.sleep(2)
            count+=1
        else :
            print("not found")
            break

def goBack():
    time.sleep(2)
    cross = driver.find_element_by_xpath('/html/body/div[5]/div[3]')
    cross.find_element_by_class_name('wpO6b').click()
    # driver.find_element_by_xpath('/html/body/div[5]/button').click()
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div').click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/article/div/div/div[1]/div[1]/a/div/div[2]').click()
    global number
    number+=1
    print(number)
    if(number == 22):
        return
    time.sleep(3)
    newTag(number)
  

def tagsLike(e):
    e.click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]').click()
    time.sleep(5)
    like_pic()
    continue_liking()
    time.sleep(3)
    goBack()

def newTag(num):
    contet = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]')
    tags = contet.find_elements_by_tag_name('a')
    count = 0
    tagsLike(tags[num])
    # for e in tags:
    #     count+=1
    #     if(count>num):
    #         tagsLike(e)
    #         break
    


driver.get("https://www.instagram.com/")
time.sleep(3)
driver.maximize_window()
# find username/email field and send the username itself to the input field
# driver.find_element_by_name("login").send_keys("hello")
# find password input field and insert password as well
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
# click login button
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(6)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(4)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/article/div/div/div[1]/div[1]/a/div/div[2]').click()
time.sleep(3)
newTag(number)