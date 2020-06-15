# 尚硅谷高级MySQL

视频地址：https://www.bilibili.com/video/BV1KW411u7vy?p=1

### 08 MySQL逻辑架构简介

4层结构

1.连接层

2.服务层

3.引擎层

4.存储层

### 09 存储引擎简介

![image-20200511214446000](images\微信图片_20200511214432.png)

###  10 SQL性能下降原因

查询语句写的懒

索引失效 

​	单值索引

​		```create index idx_user_name on user(name)```

​	复合索引

​		```create index idex_user_name on user(name, email)```

关联查询太多join

服务器调优和各个参数

### 11 sql加载顺序

sql执行顺序

手写 

机读 

from 

on 

where  

group by order by having 

select 

总结

![image-20200511214446000](images\微信图片_20200518223940.png)