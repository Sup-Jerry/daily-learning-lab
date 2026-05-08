# C++ 入门笔记

## 基本结构

一个最简单的 C++ 程序通常包含头文件、主函数和输出语句。

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, C++!" << endl;
    return 0;
}
```

## 变量

C++ 需要先声明变量类型。

```cpp
int age = 20;
double score = 88.5;
string name = "Jerry";
```

## 条件判断

`if` 语句用于处理分支逻辑。

```cpp
int score = 75;
if (score >= 60) {
    cout << "pass" << endl;
} else {
    cout << "fail" << endl;
}
```

## 循环

`for` 循环适合处理固定次数的重复任务。

```cpp
for (int i = 0; i < 3; i++) {
    cout << i << endl;
}
```

## vector

`vector` 是常用的动态数组，适合初学阶段练习存储和遍历。

```cpp
#include <vector>
vector<int> nums = {1, 2, 3};
for (int num : nums) {
    cout << num << endl;
}
```

## 编译与运行

写完程序后，需要先编译，再执行生成的程序。

```bash
g++ main.cpp -o main
./main
```

## 学习提醒

- 注意分号、花括号和类型声明
- 遇到编译错误时，先看第一条错误信息
- 不要一下写太长的程序，先从小示例开始
