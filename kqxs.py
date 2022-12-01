__doc__ = r"""
Script kiểm tra xem các số argument đầu vào có trúng lô không
(2 số cuối trùng với một giải nào đó). Nếu không có argument nào thì print
ra tất cả các giải từ đặc biệt -> giải 7.
Lấy kết quả từ trang web tùy ý ví dụ ketqua.net ketqua.vn
Dạng của câu lệnh::
  ketqua.py [NUMBER1] [NUMBER2] [...]
"""

import time
import sys
import requests
import bs4
import re
import datetime


url = "https://ketqua.vn/"
r = requests.get(url)
tree = bs4.BeautifulSoup(markup=r.text, features="html.parser")
prizes = tree.find_all("td", class_=re.compile("prize"))
result_raw = [prize.text.strip() for prize in prizes]
list_two_last_digits = [prize[-2:] for prize in result_raw]


def check_numbers(numbers):
    result = None
    set_numbers = set()
    for number in list(numbers):
        if number in list_two_last_digits:
            set_numbers.add(number)

    result = set_numbers
    return result


def solve(input_data):
    result = None

    if len(input_data) > 0:
        result = check_numbers(input_data)
        for number in input_data:
            if number in result:
                print("Số {} trúng {} nháy.".format(number, list_two_last_digits.count(number)))
            else:
                print("Số {} không trúng giải.".format(number))
    elif len(input_data) == 0:
        result = [int(prize) for prize in result_raw]
        # result_day = datetime.date.result_day().strftime("%d/%m/%Y")
        result_day = tree.find('div', {'class': 'color-content text-center fw-normal'}).text
        print("Kết quả xổ số Miền Bắc {}, giải ĐB đến G7: {}".format(result_day, result))
        print()
        for num in set(list_two_last_digits):
            if list_two_last_digits.count(num) > 1:
                print('Lô về nhiều nhất: {} với {} nháy'.format(num, list_two_last_digits.count(num)))


    return result


def main():
    numbers = []
    num_cal = input('Bạn có mấy con lô: ')
    if num_cal:
        for i in range(int(num_cal)):
            numbers.append(input('Nhập lô vào: '))
    elif num_cal == '' or num_cal == None:
        print('Không đánh thì xem kết quả cũng được mà nhỉ!')
        print()
        time.sleep(2)

    for arg in sys.argv[1:]:
        print(sys.argv[0])
        if arg.isdigit():
            numbers.add(int(arg))
        else:
            print("Giá trị {} không phải là số.".format(arg))

    solve(numbers)


if __name__ == "__main__":
    main()