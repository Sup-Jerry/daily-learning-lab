# 前端基础笔记

## HTML：页面结构

HTML 用来描述页面上有什么内容，比如标题、段落、列表和按钮。

```html
<h1>My Study Page</h1>
<p>This is a simple note.</p>
```

## CSS：页面样式

CSS 用来控制颜色、间距、字体和布局。

```css
body {
    font-family: Arial, sans-serif;
}

h1 {
    color: #3366cc;
}
```

## JavaScript：页面交互

JavaScript 用来处理点击、数据变化和简单逻辑。

```javascript
const name = "Jerry";
console.log(`Hello, ${name}`);
```

## 数组基础

数组适合保存多个值，也常配合 `map`、`filter` 等方法使用。

```javascript
const numbers = [1, 2, 3, 4];
const doubled = numbers.map((item) => item * 2);
console.log(doubled);
```

## DOM 基础理解

DOM 可以理解为浏览器把页面内容组织成一棵结构树，JavaScript 可以通过它读取或修改页面元素。

```javascript
const title = document.querySelector("h1");
console.log(title.textContent);
```

## 学习提醒

- 先搞清楚 HTML、CSS、JavaScript 的分工
- 先写小页面，再逐步增加交互
- 多看浏览器控制台输出，帮助理解代码执行结果
