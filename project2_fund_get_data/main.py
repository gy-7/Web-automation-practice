from utils.get_data import get_fund_data
from utils.visiual_res import visiual_all_fund_data

# 删除不想查看的数据
def data_ops(fund_data_header, fund_data):
    fund_data_header = fund_data_header[2:-1]
    for i in range(len(fund_data_header)):
        if fund_data_header[i] == '净值':
            fund_data_header[i - 1] += '净值'
        elif fund_data_header[i] == '长率':
            fund_data_header[i - 1] += '长率'

    fund_data_header.remove('净值')
    fund_data_header.remove('净值')
    fund_data_header.remove('长率')
    return fund_data_header, fund_data


if __name__ == '__main__':
    fund_data_header, fund_data = get_fund_data()
    fund_data_header, fund_data = data_ops(fund_data_header, fund_data)

    visiual_all_fund_data(fund_data_header, fund_data)
