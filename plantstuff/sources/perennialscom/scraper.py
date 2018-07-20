import requests

from plantstuff.core import conf, fetch
from plantstuff.core.decorators import to_json

URL = 'http://www.perennials.com/plants/{plant}.html'

get_dom = fetch.get_dom(directory='../../data/perennialscom')

# @to_json(directory='../../data/perennialscom')
# def get_count_of_pages():
#     """Figure out how many pages are available for each letter."""
#     res = {}
#     for letter in conf.LETTERS:
#         content, dom = get_dom(
#             'http://www.perennials.com/results_alphabet.html?'
#             'start=0&letter={letter}'.format(letter=letter)
#         )
#         # Find the number of results shown, to determine how many
#         # calls to make.
#         dom.find('')
#     return res


# # @to_json(directory='../../data/perennialscom')
# def guess_plant():
#     """Download api data by plant symbol for ALL plants."""
#     per_page = 96
#     content, dom = get_dom(
#         'http://www.perennials.com/results_alphabet.html?'
#         'start=0&letter={letter}'.format(letter='A')
#     )
#     for letter in conf.LETTERS:
#         pages_per_letter =
#         print(letter)

#     urls = []


if __name__ == '__main__':
    get_count_of_pages()
