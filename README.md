# format_json
python script for formatting json string.

# How to use

## case1
std output to this python script.

```console
$ echo '{"name":"佐藤"}' | python format_json.py 
{
    "name": "佐藤"
}
```

## case2
set $HOME/bin to PATH.

```bash:bashの設定ファイル
PATH=$PATH:$HOME/bin
```

```console:$HOME/bin
$ ls -la $HOME/bin
total 8
drwxr-xr-x 2 xxxx xxxx 4096 Nov 16 09:26 .
drwxr-xr-x 7 xxxx xxxx 4096 Nov 16 11:13 ..
lrwxrwxrwx 1 xxxx xxxx   49 Nov 16 09:26 fj -> /path/to/format_json.py
```

You can use this script as below.

```console
$ echo '{"name":"佐藤"}' | fj
{
    "name": "佐藤"
}
```
If you use this approach then please change this script's shebang to suitable.
