"""
    This is sandbox file for learning and exercise purposes.
"""

cube = -66
guess = None
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube', guess)
else:
    if cube < 0:
        guess = -guess
    print(f'Cube root of {cube} is {guess}')


DATE_FORMAT = "%m/%d/%y %H:%M"

import datetime
a = "7/2/10 2:00"
# b = "2012"
c = "2012-01"
d = "2012-02-02"

print(datetime.datetime.strptime(a, DATE_FORMAT))
# print(datetime.datetime.strptime(b, DATE_FORMAT))
print(datetime.datetime.strptime(c, DATE_FORMAT))
print(datetime.datetime.strptime(d, DATE_FORMAT))


import requests

terms = {'q': 'flowers', 'inauthor': 'Keyes'}
response = requests.get(
    'https://www.googleapis.com/books/v1/volumes',
    params=terms,
)

url = response.url.replace('&', '+')
response = requests.get(url)
print(response.url)
print(response.text)


