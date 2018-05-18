import requests


class CurrencyConverter:
    def __init__(self):
        self._url = 'http://www.floatrates.com/daily/'

    def convert(self, cur_from, cur_to, amount):
        url = self._url + cur_from + '.json'

        response = requests.get(url)
        data = response.json()

        return data[cur_to]['rate'] * amount


def main():
    cur_converter = CurrencyConverter()
    amount_euro = 1569.7

    print(cur_converter.convert('eur', 'usd', amount_euro))


main()
