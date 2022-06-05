import csv

from typing import List


def read_csv(file_path: str, have_header=True) -> csv.reader:
    """
    读取csv文件，返回csv.reader对象
    @param file_path: csv文件路径
    @param have_header: 是否有表头，默认有
    @return:
    """
    file = open(file_path, 'r', encoding='utf-8')
    csv_file = csv.reader(file)
    csv_data = list(csv_file)
    if have_header:
        return csv_data[1:]
    return csv_data


def save_csv(file_path, data: List[List[str]], header: List[str]=None):
    """
    保存csv文件
    @param file_path: 保存路径
    @param header: 表头
    @param data: 内容数据
    @return:
    """
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(data)


if __name__ == '__main__':
    file_path = "./samples_res.csv"
    header = ["函数", '起始站', '终点站', '订票日期', '姓名', '手机号', '函数耗时']
    data = [['booking_a_train_ticket', '北京', '上海', '1', '张三', '13888888888', '15.003'],
            ['booking_a_train_ticket', '北京', '上海', '1', '张三', '13888888888', '15.003'],
            ['booking_a_train_ticket', '北京', '上海', '1', '张三', '13888888888', '15.003'],
            ['booking_a_train_ticket', '北京', '上海', '1', '张三', '13888888888', '15.003']]
    save_csv(file_path, header, data)
