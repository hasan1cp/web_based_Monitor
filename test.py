import re
a = '172.16.0.22 - - [30/Apr/2026:11:11:26 +0000] "POST /static/css/main.css HTTP/1.1" 301 2951'


status = r'\"\s(\d{3})'

statuss = re.search(status, a)

print(statuss.group(1))
