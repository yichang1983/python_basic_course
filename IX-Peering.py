import re

name = ""
asn = ""
ipv4_address = ""
ipv6_address = ""
counter = 0

with open('/Users/yichangchen/desktop/3.txt', 'r') as file:
    for line in file:
        stripped_line = line.strip()
        # Check if the line contains at least 2 consecutive numbers and no . and no : # # ^ 是指匹配输入字符串的开始位置，[a-zA-Z] 是指字符范围，{2,} 是指至少二個英文字母, stripped_line 是指找尋的內容。匹配一个数字字符, 等价于 [0-9], {2,} 是指至少二個数字字符，
        if not re.search(r'\d{2}', stripped_line) and not re.search(r'\.', stripped_line) and not re.search(r':', stripped_line):
            print()
            name = stripped_line
            print("Name:", name)
        elif not re.search(r'[a-zA-Z]', stripped_line) and not re.search(r'\.', stripped_line) and not re.search(r':', stripped_line):
            asn = stripped_line
            print("ASN:", asn)
        elif re.search(r'\.', stripped_line) and not re.search(r'[a-zA-Z]', stripped_line) and not re.search(r':', stripped_line):
            ipv4_address = stripped_line
            print("IPv4 address:", ipv4_address)
        elif ':' in line:
            ipv6_address = stripped_line
            print("IPv6 address:", ipv6_address)



