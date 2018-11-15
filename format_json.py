#!/usr/bin/python
# coding: UTF-8
import json

arg = json.loads(raw_input())
formatted_json = json.dumps(
    arg,
    ensure_ascii=False,
    indent=4,
    separators=(',', ': '))

print formatted_json