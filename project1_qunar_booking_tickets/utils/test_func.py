# 时间装饰器
import time
from datetime import date, timedelta
from typing import List

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .visiual_res import visiual_res


def get_date(n):
    return str(date.today() + timedelta(days=n))


def booking_a_train_ticket(start, end, date_offset, name, phone):
    start_time = time.time()  # ----->函数运行前时间
    driver = webdriver.Edge()
    url = "https://train.qunar.com/"

    driver.get(url)
    # 最大化，显式等待
    WebDriverWait(driver, 3, poll_frequency=0.2).until(
        EC.presence_of_element_located((By.ID, "js-con")))
    # time.sleep(1)
    driver.maximize_window()

    # 点击事件
    action = ActionChains(driver)

    # 输入出发地
    driver.find_element_by_xpath("//*[text()='出发']/../input").send_keys(start)
    action.move_by_offset(0, 0)
    action.click()
    action.perform()

    # 输入目的地
    driver.find_element_by_xpath("//*[text()='到达']/../input").send_keys(end)
    action.move_by_offset(0, 0)
    action.click()
    action.perform()

    # 三种方法，那个有效用哪个
    # 方法1：删除默认日期
    # for i in range(10):
    #     driver.find_element_by_xpath("//*[text()='日期']/../input").send_keys(Keys.BACKSPACE)

    # 方法2：删除默认日期
    driver.find_element_by_xpath("//*[text()='日期']/../input").send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_xpath("//*[text()='日期']/../input").send_keys(Keys.BACKSPACE)

    # 方法3：删除默认日志
    # driver.find_element_by_xpath("//*[text()='日期']/../input").clear()

    if isinstance(date_offset, str):
        date_offset = int(date_offset)
    date_val = get_date(date_offset)

    # 输入日期
    driver.find_element_by_xpath("//*[text()='日期']/../input").send_keys(date_val)
    action.move_by_offset(0, 0)
    action.click()
    action.perform()

    # 点击搜索
    driver.find_element('name', 'stsSearch').click()

    # 点击第一个火车票，购买，显式等待
    # WebDriverWait(driver, 3, poll_frequency=0.2).until(EC.presence_of_element_located(
    #     (By.XPATH, '//*[@id="list_listInfo"]/ul[2]/li[1]/div/div[7]/a[1]')))

    WebDriverWait(driver, 3, poll_frequency=0.2).until(EC.presence_of_element_located(
        (By.CLASS_NAME, 'js_listinfo')))

    driver.find_element_by_xpath('//*[@id="list_listInfo"]/ul[2]/li[1]/div/div[7]/a[1]').click()

    # 填写姓名，手机号码，显式等待
    WebDriverWait(driver, 3, poll_frequency=0.2).until(EC.presence_of_element_located(
        (By.XPATH, '//*[text()="姓名（必填）"]/../input')))
    driver.find_element_by_xpath('//*[text()="姓名（必填）"]/../input').send_keys(name)
    driver.find_element_by_xpath('//*[text()="手机号码（必填）"]/../input').send_keys(phone)

    time.sleep(1)

    # 关闭当前页面
    driver.close()

    # 关闭浏览器
    # driver.quit()

    end_time = time.time()  # ----->函数运行后时间
    cost_time = end_time - start_time  # ---->运行函数消耗时间
    data = ["booking_a_train_ticket", start, end,
            str(date_val), name, phone, str(round(cost_time, 3))]
    visiual_res(data)
    return data


def booking_train_tickets(data: List[str]):
    res = []
    for i in range(len(data)):
        res.append(booking_a_train_ticket(*data[i]))
    return res
