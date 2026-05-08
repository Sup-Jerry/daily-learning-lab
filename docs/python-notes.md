# Python 入门笔记

## 变量与基本类型

Python 常见基础类型有整数、浮点数、字符串和布尔值。

```python
name = "Jerry"
age = 20
is_learning = True
print(name, age, is_learning)
```

## 列表

列表可以保存一组有顺序的数据，也能进行遍历和修改。

```python
languages = ["Python", "C++", "JavaScript"]
languages.append("Git")
for item in languages:
    print(item)
```

## 条件判断

条件语句用于根据不同情况执行不同代码。

```python
score = 78
if score >= 60:
    print("pass")
else:
    print("fail")
```

## 循环

`for` 适合遍历列表，`while` 适合重复执行直到条件变化。

```python
for i in range(3):
    print("loop", i)
```

## 函数

函数可以把重复逻辑封装起来，方便多次调用。

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Jerry"))
```

## 文件读写

文件操作是 Python 很常见的基础练习。

```python
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("study notes")
```

## 学习提醒

- 先理解语法，再逐步练习组合使用
- 每次写完脚本都自己运行一遍
- 报错时先看报错行号和提示信息
