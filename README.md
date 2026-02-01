# Duration Parser

一个极简的时长字符串解析器：把类似 `1h30m`、`2d 3h` 这样的输入解析成**秒**。

## 使用方法

```bash
python -c "from duration_parser import parse_duration_seconds as p; print(p('1h30m'))"
```

## 运行测试

```bash
python -m unittest -v
```