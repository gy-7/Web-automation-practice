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
