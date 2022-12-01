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


def lottery_results():
    result = None

    url = "https://ketqua.vn"
    r = requests.get(url)
    tree = bs4.BeautifulSoup(markup=r.text, features="html.parser")
    prizes = tree.find_all("td", class_=re.compile("prize"))

    result = [prize.text.strip() for prize in prizes]

    return result


def check_numbers(numbers):
    result = None

    set_two_last_digits = set([prize[-2:] for prize in lottery_results()])

    set_numbers = set()
    for number in list(numbers):
        if number in set_two_last_digits:
            set_numbers.add(number)

    result = set_numbers
    return result


def solve(input_data):
    result = None

    if len(input_data) > 0:
        result = check_numbers(input_data)
        for number in input_data:
            if number in result:
                print("Số {} trúng {} nháy.".format(number, input_data.count(number)))
            else:
                print("Số {} không trúng giải.".format(number))
    elif len(input_data) == 0:
        result = [int(prize) for prize in lottery_results()]
        today = datetime.date.today().strftime("%d/%m/%Y")
        print(
            "Kết quả xổ số ngày {}, giải ĐB đến G7: {}".format(today, result)
        )

    return result


def main():
    numbers = []
    num_cal = input('Bạn có mấy con lô: ')
    if num_cal:
        for i in range(int(num_cal)):
            numbers.append(input('Nhập lô vào: '))
    else:
        print('Nếu không đánh lô thì xem thôi!')
        time.sleep(1)

    for arg in sys.argv[1:]:
        print(sys.argv[0])
        if arg.isdigit():
            numbers.add(int(arg))
        else:
            print("Giá trị {} không phải là số.".format(arg))

    solve(numbers)


if __name__ == "__main__":
    main()