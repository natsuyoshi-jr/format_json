#!/usr/bin/env python
# coding: utf-8
import sys
import codecs
import json

# 標準出力をラップして常にutf-8で出力する
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

# パイプで渡された値を受け取る
standard_output_value = sys.stdin.readline()

# 文字列がjson形式かチェック
try:
    # 文字列をjsonデコード
    json_string = json.loads(standard_output_value)
except ValueError:
    # 文字列がjson形式でないことをターミナルに出力
    sys.stdout.write("No JSON object could be decoded")
    # エラーコードを返し処理を終了
    sys.exit(1)

# jsonを整形する
# ensure_asciiをFalseにすることで非asciiに対応させる
formatted_json = json.dumps(json_string,
                            ensure_ascii=False,
                            indent=4,
                            separators=(',', ': '))
# ターミナルに整形したjsonを出力する
sys.stdout.write(formatted_json)
# 正常コードを返し処理を終了
sys.exit(0)