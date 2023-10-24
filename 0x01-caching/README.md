# 0x01. Caching
`Back-end` `Caching` 

## Learning Outcomes
- I learned what caching means.
- I learned what a cache replacement policy is.
- I learned what FIFO means.
- I learned what LIFO means.
- I learned what LRU means.
- I learned what MRU means.
- I learned what LFU means.

## Tasks
### [0. Basic dictionary](./0-basic_cache.py)
I implemented a `BasicCache` class that inherits from `BaseCaching` and is a caching system:

#### Output
```
simontagbor@ubuntu:~/0x01$ cat main.py
#!/usr/bin/env python3
""" Main file """
BasicCache = __import__('0-basic_cache').BasicCache

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))

simontagbor@ubuntu:~/0x01$ ./main.py
Current cache:
Current cache:
A: Hello
B: World
C: Holberton
Hello
World
Holberton
None
Current cache:
A: Hello
B: World
C: Holberton
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery
Street
simontagbor@ubuntu:~/0x01$
```

### [1. FIFO caching](./1-fifo_cache.py)
I implemented a `FIFOCache` class that inherits from `BaseCaching` and is a caching system:

#### Output
```
simontagbor@ubuntu:~/0x01$ cat main.py
#!/usr/bin/env python3
""" Main file """
FIFOCache = __import__('1-fifo_cache').FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()

simontagbor@ubuntu:~/0x01$ ./main.py
A: Hello
B: World
C: Holberton
D: School
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
DISCARD: B
Current cache:
C: Street
D: School
E: Battery
F: Mission

simontagbor@ubuntu:~/0x01$
```

