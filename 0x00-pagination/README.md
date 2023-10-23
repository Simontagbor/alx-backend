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
