import pytest

from utils.data_func import read_csv, save_csv
from utils.test_func import booking_a_train_ticket, booking_train_tickets
from utils.visiual_res import visiual_res, visiual_all_res

file_path = "./samples/booking_a_train_ticket_samples.csv"
save_res_path = "./samples/booking_a_train_ticket_samples_res.csv"
data=read_csv(file_path)

# def book_tickets():
#     """
#     通过rich可视化最终数据，并保存到csv文件中。
#     @return:
#     """
#     data = read_csv(file_path)
#     save_res_path= "./samples/booking_train_tickets_samples_res.csv"
#     data_res = booking_train_tickets(data)
#     header = ["函数", '起始站', '终点站', '订票日期', '姓名', '手机号', '函数耗时']
#     visiual_all_res(header, data_res)
#     save_csv(save_res_path, data_res, header)

@pytest.mark.parametrize("data", data)
def test_book_ticket(data):
    booking_a_train_ticket(*data)

if __name__ == '__main__':
    pytest.main("-s", "main.py")
    # book_tickets()


"""
单元测试结果：

============================= test session starts =============================
collecting ... collected 12 items

main.py::test_book_ticket[data0] 
main.py::test_book_ticket[data1] 
main.py::test_book_ticket[data2] 
main.py::test_book_ticket[data3] 
main.py::test_book_ticket[data4] 
main.py::test_book_ticket[data5] 
main.py::test_book_ticket[data6] 
main.py::test_book_ticket[data7] 
main.py::test_book_ticket[data8] 
main.py::test_book_ticket[data9] 
main.py::test_book_ticket[data10] 
main.py::test_book_ticket[data11] 

======================= 12 passed in 248.06s (0:04:08) ========================

进程已结束,退出代码0
PASSED                                  [  8%]booking_a_train_ticket 北京 天津 2022-06-06 张三 13888888888 12.491
PASSED                                  [ 16%]booking_a_train_ticket 天津 北京 2022-06-07 李四 13999999999 43.311
PASSED                                  [ 25%]booking_a_train_ticket 北京 天津 2022-06-08 王五 13777777777 15.235
PASSED                                  [ 33%]booking_a_train_ticket 北京 天津 2022-06-09 赵六 13666666666 14.293
PASSED                                  [ 41%]booking_a_train_ticket 天津 北京 2022-06-10 钱七 13555555555 43.443
PASSED                                  [ 50%]booking_a_train_ticket 北京 天津 2022-06-11 孙八 13444444444 13.243
PASSED                                  [ 58%]booking_a_train_ticket 北京 天津 2022-06-12 周九 13333333333 12.216
PASSED                                  [ 66%]booking_a_train_ticket 天津 北京 2022-06-13 吴十 13222222222 12.888
PASSED                                  [ 75%]booking_a_train_ticket 北京 天津 2022-06-14 郑十一 13111111111 42.053
PASSED                                  [ 83%]booking_a_train_ticket 北京 天津 2022-06-15 王十二 1300000000 12.858
PASSED                                 [ 91%]booking_a_train_ticket 天津 北京 2022-06-16 赵十三 12999999999 12.541
PASSED                                 [100%]booking_a_train_ticket 北京 天津 2022-06-17 钱十四 12888888888 13.215

"""