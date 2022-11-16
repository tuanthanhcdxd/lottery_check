#!/usr/bin/env python3

__doc__ = r"""
Script kiểm tra xem các số argument đầu vào có trúng lô không
(2 số cuối trùng với một giải nào đó). Nếu không có argument nào thì print
ra tất cả các giải từ đặc biệt -> giải 7.

Lấy kết quả từ trang web tùy ý ví dụ ketqua.net ketqua.vn
Dạng của câu lệnh::

  ketqua.py [NUMBER1] [NUMBER2] [...]
"""

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

    list_prize = []
    for prize in prizes:
        list_prize.append(prize.text.strip())

    result = list_prize
    return result
    pass


def check_numbers(numbers):
    result = None

    set_two_last_digits = set()
    for prize in lottery_results():
        set_two_last_digits.add(int(prize[-2:]))

    set_numbers = set()
    for number in numbers:
        if number in set_two_last_digits:
            set_numbers.add(number)

    result = set_numbers
    return result
    pass


def solve(input_data):
    result = None

    if len(input_data) > 0:
        result = check_numbers(input_data)
        for number in input_data:
            if number in result:
                print("Số {} trúng giải.".format(number))
            else:
                print("Số {} không trúng giải.".format(number))
    elif len(input_data) == 0:
        result = [int(prize) for prize in lottery_results()]
        today = datetime.date.today().strftime("%d/%m/%Y")
        print(
            "Kết quả xổ số ngày {}, giải ĐB đến G7: {}".format(today, result)
        )

    return result
    pass


def main():

    numbers = set()
    for arg in sys.argv[1:]:
        if arg.isdigit():
            numbers.add(int(arg))
        else:
            print("Giá trị {} không phải là số.".format(arg))

    solve(numbers)
    pass


if __name__ == "__main__":
    main()
