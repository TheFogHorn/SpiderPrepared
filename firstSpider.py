from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.set_page_load_timeout(30)
browser.get('http://www.17huo.com/?mod=search&code=main&cid=0&market=0&keyword=%E5%A5%B3%E5%BC%8F%E5%A4%A7%E8%A1%A3&page=1')
page_info = browser.find_element_by_css_selector('body > div.wrap > div.pagem.product_list_pager > div')
print(page_info.text)
#共 3 页,每页 24 条
pages = int((page_info.text.split(',')[0]).split(' ')[1])
#a = page_info.text.split(',')
#print(pages,a)
for page in range(pages):
    url = 'http://www.17huo.com/?mod=search&code=main&cid=0&market=0&keyword=%E5%A5%B3%E5%BC%8F%E5%A4%A7%E8%A1%A3&page='+str(page+1)
    browser.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    goods = browser.find_element_by_css_selector('body > div.wrap > div:nth-child(2) > div.p_main > ul').find_elements_by_tag_name('li')
    print('%d页有%d件商品' % ((page + 1), len(goods)))
    for good in goods:
            title = good.find_element_by_css_selector('a:nth-child(1) > p:nth-child(2)').text
            #price = good.find_element_by_css_selector('div > a > span').text
            num = good.find_element_by_css_selector('a:nth-child(1) > p.item_info.item_title > span').text
            print(title)
            #print(price)
            print(num)
