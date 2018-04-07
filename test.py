#!/usr/bin/env python

import argparse, urllib.parse, base64, urllib.request, json

gfwlist_url = 'https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt'

def test():
    with open('pac.txt', 'r') as f:
        pac_temp = f.read()
    tmp_list = []
    with urllib.request.urlopen(gfwlist_url) as f:
        content = f.read()
    content = str(base64.b64decode(content), encoding='utf-8')
    content = content.splitlines(False)
    for c in content:
        if c and c[0] != '!' and c.replace('\r', '').replace('\n', '') != '' and '[' not in c and ']' not in c:
            tmp_list.append(c)
    pac_temp = pac_temp.replace("__RULES_LIST__", json.dumps(tmp_list, indent=2))
    with open('tt.pac', 'w') as f:
        f.write(pac_temp)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='', help='path to gfwlist')
    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    test()
