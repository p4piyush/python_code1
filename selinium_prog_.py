import time

from selenium import webdriver

driver_path = 'E:\\temp_python_work\\flask_client\\selenium_assignment\\driver\\chromedriver.exe'

def launch_page():
    entered_url = 'https://demo.borland.com/gmopost/'
    chrome_driver = webdriver.Chrome(executable_path=driver_path)
    chrome_driver.get('https://demo.borland.com/gmopost/')
    chrome_driver.maximize_window()

    print('Launch the side--> confirm kiya hai -- page is opened using automation..!')
    x = False
    try:
        x = chrome_driver.find_element_by_name('bSubmit') # exception ya fir-- webelement
    except:
        print('No element Found...')

    assert x!=False

    current_url = chrome_driver.current_url
    assert current_url == entered_url


    print('Verify Page2--')
    chrome_driver.find_element_by_name('bSubmit').click()
    assert chrome_driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/h1').text == 'OnLine Catalog'
    assert chrome_driver.current_url == 'https://demo.borland.com/gmopost/online-catalog.htm'

    print('Step3..')

    table_info = chrome_driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/div/center/table')
    rows = table_info.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
    count = 1
    product_with_unit_price_online_catelog = {}


    for row in rows[1:]:
        columns = row.find_elements_by_tag_name('td')
        columns[-1].find_element_by_tag_name('input').send_keys(str(count))
        product_with_unit_price_online_catelog[columns[1].text] = (columns[2].text,float(columns[2].text.split("$")[-1])*count)
        count = count + 1

    print('----Online Catelog---')
    print(product_with_unit_price_online_catelog)
    print('-------')
    chrome_driver.find_element_by_name('bSubmit').click()

    print('3rd page verify...!')
    assert chrome_driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/h1').text == 'Place Order'
    table_info = chrome_driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td/div/center/table')
    rows = table_info.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
    product_with_unit_price_place_order = {}


    for row in rows[1:]:
        columns = row.find_elements_by_tag_name('td')
        if len(columns) != 5:
            continue
        #columns[-1].find_element_by_tag_name('input').send_keys(str(count))
        product_with_unit_price_place_order[columns[1].text] = (columns[3].text, float(columns[4].text.split("$")[-1]))


    #dict1 -- Dict2 -->
    #dict2 values - grandtotal..


    grand_total = rows[-1].find_element_by_tag_name('td')[-1].text



    print('----Place Order---')
    print(product_with_unit_price_place_order)
    print('-------')
    return chrome_driver


if __name__ == '__main__':
    launch_page()
    time.sleep(30)

