from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchWindowException
import time
import requests

# 訪問網頁
driver = webdriver.Chrome()
url = 'http://cc.ee.ntu.edu.tw/~farn/courses/ST/2021.Spring/'
driver.get(url)

# 定義不同螢幕尺寸的測試
screen_sizes = [(1920, 1080)]  # 可以根據需要添加其他尺寸 (1366, 768), (768, 1024)

for width, height in screen_sizes:
    driver.set_window_size(width, height)
    time.sleep(1)

    count = 0
    error = 0
    unchecked = 0

    error_report = {}

    hrefs = []
    elements = driver.find_elements(By.TAG_NAME, 'a')
    for element in elements:
        if element.is_displayed():
            hrefs.append(element.get_attribute("href"))

    with open('result.txt', 'w') as file:
        original_window = driver.current_window_handle

        for href in hrefs:
            if href and isinstance(href, str):

                try:
                    driver.get(href)  # 訪問鏈接
                    time.sleep(1)  # 等待頁面加載

                    try:
                        response = requests.get(href)
                        status_code = response.status_code
                        print(f'<a> {count+1}\n{href}\n{status_code}')
                        file.write(f'<a> {count+1}\n{href}\n{status_code}\n')
                        if status_code == 404:
                            error += 1
                            driver.save_screenshot(f"screenshot_{error}.png")

                    except requests.exceptions.RequestException:
                        print(f'<a> {count+1}\n{href}\nRequestException\n')
                        file.write(f'<a> {count+1}\n{href}\nRequestExceptionL\n')
                        error += 1

                    

                except NoSuchWindowException:
                    print(f'<a> {count+1}\n{href}\nWindow closed unexpectedly\n')
                    file.write(f'<a> {count+1}\n{href}\nWindow closed unexpectedly\n')
                    driver.switch_to.window(original_window)
                    error += 1
                
                except StaleElementReferenceException:
                    print(f'<a> {count+1}\n{href}\nStaleElementReferenceExceptio\n')
                    file.write(f'<a> {count+1}\n{href}\nStaleElementReferenceExceptio\n')
                    error += 1
            
            else:
                error_report[count] = 'invalid URL'
                print(f'<a> {count+1}\n{href}\nInvalid URL\n')
                file.write(f'<a> {count+1}\n{href}\nInvalid URL\n')
                error += 1
            
            count += 1

        print("The number of <a>: ", count)
        print("The number of error in <a>: ", error)
        print("The number of <a> (unchecked): ", unchecked)

    driver.get(url)  # 返回原始頁面

driver.quit() # 關閉瀏覽器