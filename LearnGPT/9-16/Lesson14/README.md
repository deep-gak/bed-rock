数据库开发 - 快速生成数据库代码
===========================

## 知识点

* 从数据库标记语言(DBML)快速生成数据库代码

## 官网

https://dbml.dbdiagram.io/home/

## 实战演习/说明讲解

>画面演示

+ 使用 DBML 设计数据库模式
+ 根据 DBML 生成数据库代码

## 操作步骤

### 使用 DBML 设计数据库模式

__建立数据库ER图__

https://dbdiagram.io/

**Create your diagram**

### 提示词:根据 DBML 生成数据库代码

请根据下面的DBML帮我生成SQL建表文，数据库使用mysql

```dbml
Table follows {
  following_user_id integer
  followed_user_id integer
  created_at timestamp 
}

Table users {
  id integer [primary key]
  username varchar
  age integer
  role varchar
  created_at timestamp
}

Table posts {
  id integer [primary key]
  title varchar
  body text [note: 'Content of the post']
  user_id integer
  status varchar
  created_at timestamp
}

Ref: posts.user_id > users.id // many-to-one

Ref: users.id < follows.following_user_id

Ref: users.id < follows.followed_user_id
```

### 提示词:生成数据表操作Python代码

请按照下列要求生成users表的根据主键的CRUD操作数据的类文件

1.使用Python语言
2.数据库使用mysql
3.类构造函数接受db数据库对象
4.生成改类的使用例子

### 提示词:生成数据表操作Go代码

请按照下列要求生成users表的根据主键的CRUD操作数据的类文件

1.使用Go语言，并使用gorm框架
2.数据库使用mysql
3.类构造函数接受db数据库对象
4.生成改类的使用例子

### 提示词:查询数据SQL

请帮我生成SQL文，取得所有id小于100的用户记录

### 提示词:修改表结构

请帮我生成SQL文，在users表中增加一个address字段，类型是varchar，并允许空值NULL。

### 提示词:从CREATE文生成DBML

请根据下面的SQL文生成DBML描述

```sql
CREATE TABLE customers (
  id INT PRIMARY KEY,
  username VARCHAR(255),
  age INT,
  address VARCHAR(255),
  role VARCHAR(255),
  created_at TIMESTAMP
);
```

Done.

## 小马部落

https://discord.gg/VSKw72P

## 课程文件

+ 小马部落Discord专区共享(四级会员)

## 小马视频频道

https://komavideo.com

## 深学AWS

https://deeplearnaws.com

## 深学Azure

https://deeplearnazure.com/

## 深学GCP

https://deeplearngcp.com/

## Youtube

https://youtube.com/@deeplearncloud

