"""
                有符号范围   无符号范围

tinyint 1字节     -128~127    0~255
int     4字节
float   4字节
double  8字节
decimal(M,D)
例如 decimal(6,2) 表示最多6位，小数点后2位  -9999.99~9999.99



char        定长 效率高 默认1字符
varchar     不定长 效率偏低
blob        二进制存储
text        长文本数据
enum        存储给定的值中的一个
set         存储给定的值中的一个或多个

"""


"""

启动 登录数据库

mysql.server start
mysql -u root -p

-----------

数据库操作

show databases;查看已有库

create database Test character set utf8; 创建Test数据库，编码为utf8

use Test; 切换数据库

select database(); 查看当前使用的数据库

show create database db;  查看数据库创建语句

drop database db;  删除数据库

-----------

表操作

create table class_1903 (id tinyint unsigned); 创建表

drop table class_1903; 删除表

show tables; 查看所有表

show create table tablename; 查看创建语句

desc tablename; 查看表结构

create table interest (id int primary key auto_increment,...) 创建表

desc interest; 查看表结构

drop interest; 删除表

insert into interest values(...);  插入数据

-----------------

表字段操作  alter

alter table interest add skill varchar(15);  添加字段
alter table interest add skill varchar(15) first;
alter table interest add skill varchar(15) after 字段名;

alter table interest drop skill; 删除字段

alter table interest modify skill int; 修改数据类型

alter table interest change skill skill1 int; 修改字段名

alter table interest rename interest_1; 重命名表



"""
