### 项目使用简介

本项目根据 https://www.bilibili.com/video/BV1NM4y1K73T  学习而来。



### 项目结构：

> samples/：测试样例文件夹，我用的csv。
>
> utils/data_func.py：数据处理文件，包括数据读取，数据保存。
>
> ==utils/test_func.py==：业务逻辑代码文件，主要的业务逻辑都在这里面，核心代码。
>
> utils/visiual_res.py：可视化结果文件
>
> main.py：主文件，运行这个文件



### 使用步骤：

如果使用的Edge浏览器，可以省略步骤1。

:one: 先下载 [Edge Driver下载](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)  然后放到项目的utils/目录下面。如果使用其他浏览器，需要自行修改浏览器 Driver。

:two: 运行main.py文件

### 测试结果
```powershell
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

```