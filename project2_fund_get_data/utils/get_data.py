from selenium import webdriver


def get_fund_data():
    path = r'E:\Coding\testEngineer\Web-automation-practice\project2_fund_get_data\utils\chromedriver.exe'
    # 改为自己的绝对路径
    option = webdriver.ChromeOptions()
    # 控制是否打开浏览器
    # option.add_argument("headless")

    driver = webdriver.Chrome(path, chrome_options=option)

    url = "https://fund.jrj.com.cn/funddata/yield.shtml"

    driver.get(url)
    # driver.maximize_window()

    # str
    fund_data = driver.find_element_by_xpath('//*[@id="table_data"]/table').text
    fund_data_header = driver.find_element_by_xpath('// *[ @ id = "table_head"] / tbody / tr')

    # fund_data ops
    # str->list[str]
    fund_data = fund_data.split('\n')

    # list->list[list[str]
    for i in range(len(fund_data)):
        fund_data[i] = fund_data[i].split(' ')[:-1]

    # fund_data_header ops
    # str->list[str]
    fund_data_header = fund_data_header.text.split('\n')

    driver.quit()
    return fund_data_header, fund_data
