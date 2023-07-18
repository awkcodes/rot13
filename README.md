rot13 is a small python script that encodes and decodes text input usin ROT 13 cypher  
-------------------------------------------------------------------------------------

for reference : https://en.wikipedia.org/wiki/ROT13

#### usage 
----------

```bash
python3 encode.py 
```
this way we can use it to encode by rotating on the alphabet as is described in the wikipedia page

  
to encode text with numerical and unicode support use :  

```bash
python3 encode.py -u
```

Note that to decode text encoded with unicode you must decode with:  

```bash
python3 decode.py -u
```
