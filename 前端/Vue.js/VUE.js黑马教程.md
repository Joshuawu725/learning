# VUE.js黑马教程

地址：https://www.bilibili.com/video/BV1vE411871g?p=1

作者：Joshua

### VUE 模板语法

#### 插值表达式

<div>{{msg}}</div>

#### 指令

什么是指令？ 指令的本质就是自定义属性

指令的格式： 以v-开始

v-cloak：解决闪动问题

使用：

[v-cloak] {

display: none;

}
```ht
<div v-cloak>
{{msg}}
</div>
```

原理：先隐藏样式，然后在内存中进行值的替换，替换好之后显示最终的结果。

##### 数据绑定指令

v-text填充纯文本

相比插值表达式更简洁

v-html

存在安全问题 只能使用内部数据

v-pre填充原始信息

显示原始信息 跳过编译过程

#### 事件绑定

v-on 

```html
<input type="button"  @click='num++'/>
<button type="button"  v-on:click='functionName'>hello</button>默认携带事件对象
<button type="button"  v-on:click='functionName()'>hello</button>
```

事件函数传递

```htm
<button type="button"  v-on:click='functionName("hi",$event)'>hello</button>
```

event.target.innerHTML 

event.target.value

事件修饰符

```html
.stop阻止冒泡
<a v-on:click.stop="handle">跳转</a>
.prevent阻止默认行为
<a v-on:click.prevent="handle">跳转</a>
```

按键修饰符 用来过滤，根据不同的按键来执行对应的时间函数。

```
.enter
<input v-on:keyup.enter='submit'>
.delete
<input v-on:keyup.delete='functionName'>
```

自定义按键修饰符

```
<input v-on:keyup.keyname='submit'>
Vue.config.keyCodes.keyname = 65
自定义按键修饰符名字是自定义的，但是对应的值必须是按键对应event.keyCode值
```



#### 属性绑定

Vue处理动态属性

```
<a v-bind:href='url'>跳转</a>
```

v-model 底层实现原理

```
<input v-bind:value="msg" v-on:input="msg=$event.target.value">
```



#### 样式绑定

class样式处理

```
对象语法
<div v-bind:class="{active: isActive}"></div>
isActive true 和false
数组语法(直接操作值 该div的类名)
<div v-bind:class="[activeClass, errorClass]"></div>
data:{
activeClass: 'active',
errorClass: 'error'
}
```

先关细节

对象绑定和数组绑定结合使用

​	直接混用

```
	[activeClass, errorClass, test: isTest]
```

class绑定的值可以简化操作

```
arrClasses:['active','error']

objClass:{

active: ture,

error:ture

}
```

默认的class 如何处理？

默认的class会保留



#### 分支循环结构

v-if：元素是否渲染到页面

v-show: 控制元素样式是否显示（已渲染） 频繁显示刷新

