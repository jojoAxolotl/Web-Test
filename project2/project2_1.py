from selenium import webdriver # 導入 Selenium 的 webdriver，用於控制瀏覽器。
from selenium.webdriver.common.by import By # 導入用於定位頁面元素的方法。
from selenium.webdriver.common.keys import Keys #  導入用於模擬鍵盤按鍵的功能。
import time
import requests

driver = webdriver.Chrome()
url = 'http://cc.ee.ntu.edu.tw/~farn/courses/ST/2021.Spring/'

# 訪問網頁
driver.get(url)  # 替換成您要測試的網站URL

# 定義不同螢幕尺寸的測試
screen_sizes = [(1920, 1080)]  # 可以根據需要添加其他尺寸 (1366, 768), (768, 1024)

list = [] 

for width, height in screen_sizes:
    driver.set_window_size(width, height)
    current_size = f'{width}x{height}'
    
    time.sleep(1)

    # checklist = ['a','abbr','acronym','address','area','article','aside','audio','b','base','bdi','bdo'\
    # ,'big','blockquote','body','br','button','canvas','caption','center','cite','code','col','colgroup'\
    # ,'data','datalist','dd','del','details','dfn','dialog','dir','div','dl','dt','em','embed','fieldset'\
    # ,'figcaption','figure','font','footer','form','frame','frameset','h1','h2','h3','h4','h5','h6','head'\
    # ,'header','hgroup','hr','html','i','iframe','image','img','input','ins','kbd','label','legend','li'\
    # ,'link','main','map','mark','marquee','menu','menuitem','meta','meter','nav','nobr','noembed','noframes'\
    # ,'noscript','object','ol','optgroup','option','output','p','param','picture','plaintext','portal','pre'\
    # ,'progress','q','rb','rp','rt','rtc','ruby','s','samp','script','search','section','select','slot'\
    # ,'small','source','span','strike','strong','style','sub','summary','sup','table','tbody','td','template'\
    # ,'textarea','tfoot','th','thead','time','title','tr','track','tt','u','ul','var','video','wbr','xmp']
    
    checklist = ['a']
    count = 0

    # 打開文件，使用 'w' 表示寫入模式
    with open('result_1.txt', 'w') as file:

        for i in range(len(checklist)):
            # 例如，檢查標題元素是否可見
            elements = driver.find_elements(By.TAG_NAME, checklist[i])

            for j in range(len(elements)):
                if elements[j].is_displayed() == True:
                    count += 1

                    print('<'+checklist[i]+'>'+' '+str(j+1))
                    file.write('<'+checklist[i]+'>'+' '+str(j+1)+"\n")
                    print(elements[j].text)
                    file.write(elements[j].text+"\n")

                    href = elements[j].get_attribute("href")
                    print(href)
                    try:
                        file.write(href+"\n")
                    except:
                        file.write("No url\n")

        # 寫入文本内容
        print("The number of <"+str(checklist[i])+"> : "+str(count+1))
        file.write("The number of <"+str(checklist[i])+"> : "+str(count+1)+"\n")

    response = requests.get(url)
    html_content = response.text

        # Specify the file path and open it in write mode
    file_path = "test_page_1.html"
    with open(file_path, 'w', encoding='utf-8') as file: #
        file.write(html_content)
        print(f"HTML content saved to {file_path}")

# 關閉瀏覽器
driver.quit()