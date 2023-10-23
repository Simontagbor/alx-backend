# 0x00. Pagination
`Backend > API > Pagination`

## learning outcomes
- i learned how to paginate a dataset with simple page and page_size parameters
- i learned how to paginate a dataset with hypermedia metadata
- i learned how to paginate in a deletion-resilient manner

## Tasks
### [0. Simple helper function](./0-simple_helper_function.py)
In this task, I implemented a simple helper function to paginate a dataset.

#### Ouput:
```
simontagbor@ubuntu:~/0x04-pagination$ cat 0-main.py
#!/usr/bin/env python3
"""
Main File for Simple Helper Function
"""
index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)

simontagbor@ubuntu:~/0x04-pagination$ ./0-main.py
<class 'tuple'>
(0, 7)
<class 'tuple'>
(30, 45)
simontagbor@ubuntu:~/0x04-pagination$
```

### [1. Simple pagination](./1-simple_pagination.py)
In this task, I  implemented a method that takes two integer arguments page and page_size with a return value of a list of the appropriate page of the dataset (i.e. the correct list of rows).

#### Ouput:
```
simontagbor@ubuntu:~/0x04-pagination$ cat 1-main.py
#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('1-simple_pagination').Server

server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with negative values")

try:
    should_err = server.get_page(0, 0)
except AssertionError:
    print("AssertionError raised with 0")

try:
    should_err = server.get_page(2, 'Bob')
except AssertionError:
    print("AssertionError raised when page and/or page_size are not ints")


print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))

simontagbor@ubuntu:~/0x04-pagination$ ./1-main.py
AssertionError raised with negative values
AssertionError raised with 0
AssertionError raised when page and/or page_size are not ints
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3']]
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5']]
[]
simontagbor@ubuntu:~/0x04-pagination$
```
### [2. Hypermedia pagination](./2-hypermedia_pagination.py)
In this task, I implemented a method that takes the same arguments (and defaults) as get_page and returns a dictionary containing the following key-value pairs:
    `page_size`: the length of the returned dataset page
    `page`: the current page number
    `data`: the dataset page (equivalent to return from previous task)
    `next_page`: number of the next page, None if no next page
    `prev_page`: number of the previous page, None if no previous page
    `total_pages`: the total number of pages in the dataset as an integer

#### Ouput:
```
simontagbor@ubuntu:~/0x04-pagination$ cat 2-main.py
#!/usr/bin/env python3
"""
Main file
"""
Server = __import__('2-hypermedia_pagination').Server

server = Server()

print(server.get_hyper(1, 2))
print("---")
print(server.get_hyper(2, 2))
print("---")
print(server.get_hyper(100, 3))
print("---")
print(server.get_hyper(3000, 100))

simontagbor@ubuntu:~/0x04-pagination$

simontagbor@ubuntu:~/0x04-pagination$ ./2-main.py
{'page_size': 2, 'page': 1, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2']], 'next_page': 2, 'prev_page': None, 'total_pages': 9709}
---
{'page_size': 2, 'page': 2, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emma', '99', '4']], 'next_page': 3, 'prev_page': 1, 'total_pages': 9709}
---
{'page_size': 3, 'page': 100, 'data': [['2016', 'FEMALE', 'BLACK NON HISPANIC', 'Londyn', '14', '39'], ['2016', 'FEMALE', 'BLACK NON HISPANIC', 'Amirah', '14', '39'], ['2016', 'FEMALE', 'BLACK NON HISPANIC', 'McKenzie', '14', '39']], 'next_page': 101, 'prev_page': 99, 'total_pages': 6473}
---
{'page_size': 0, 'page': 3000, 'data': [], 'next_page': None, 'prev_page': 2999, 'total_pages': 195}
simontagbor@ubuntu:~/0x04-pagination$
```

