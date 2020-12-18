"""
                有符号范围   无符号范围
数值类型
tinyint 1字节     -128~127    0~255
int     4字节
float   4字节
double  8字节
decimal(M,D)
例如 decimal(6,2) 表示最多6位，小数点后2位  -9999.99~9999.99


字符类型
char        定长 效率高 默认1字符
varchar     不定长 效率偏低
blob        二进制存储
text        长文本数据

枚举类型
enum        存储给定的值中的一个
set         存储给定的值中的一个或多个

日期时间类型
date
time
year
datetime
timestamp

日期时间函数
NOW()
CURDATE()
YEAR(字段名)
DATE(字段名)
TIME(字段名)

日期时间运算
select * from table where 字段名 运算符 (NOW() - interval 间隔)
间隔单位  1 day | 3 month | 2 year

eg1:查询1年以前的用户充值信息
    select * from table where time < (NOW() - interval 1 year)


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


-----------------

表记录操作  

增：insert into stu(name) values("张");

删：delete from stu where score < 60;

改：select * from stu where score < 60;

查：update stu set name = '张' where id = 3;


-----------------
范围比较 
in(), not in(), between val1 and val2 

select name,score from stu where score between 0 and 59;

select name,score from stu where class in ("AID12","AID13");

-----------------
空值比较
is NULL , is not NULL

order by desc / asc

limit n : 显示前n条
limit m,n : 从第m+1条开始，显示n条

分页：每页10条，显示第6页内容
limit (61-)*10,10

"""
"""

## MySQL普通查询

    3、select ...聚合函数 from 表名
    1、where ...
    2、group by ...
    4、having ...
    5、order by ...
    6、limit ...;
    


- **聚合函数**

| 方法          | 功能                 |
| ------------- | -------------------- |
| avg(字段名)   | 该字段的平均值       |
| max(字段名)   | 该字段的最大值       |
| min(字段名)   | 该字段的最小值       |
| sum(字段名)   | 该字段所有记录的和   |
| count(字段名) | 统计该字段记录的个数 |
|               |                      |


having语句通常与group by联合使用
having语句存在弥补了where关键字不能与聚合函数联合使用的不足,
where只能操作表中实际存在的字段,having操作的是聚合函数生成的显示列

"""

"""
索引  普通(MUL) and 唯一(UNI)

创建表时添加索引：
create table 表名(    
字段名 数据类型， 
字段名 数据类型， 
index(字段名), 
index(字段名), 
unique(字段名) );


已有表中创建索引
create [unique] index 索引名 on 表名(字段名);


查看索引
1、desc 表名; --> KEY标志为：MUL 、UNI 
2、show index from 表名\G;


删除索引
drop index 索引名 on 表名;

"""