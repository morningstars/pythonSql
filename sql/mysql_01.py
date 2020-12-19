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

"""

# ***************    数据库操作   ***************

"""

show databases;查看已有库

create database Test character set utf8; 创建Test数据库，编码为utf8

use Test; 切换数据库

select database(); 查看当前使用的数据库

show create database db;  查看数据库创建语句

drop database db;  删除数据库

"""

# ***************    表操作   ***************

"""
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

"""

# ***************    表字段操作  alter   ***************

"""
表字段操作

alter table interest add skill varchar(15);  添加字段
alter table interest add skill varchar(15) first;
alter table interest add skill varchar(15) after 字段名;

alter table interest drop skill; 删除字段

alter table interest modify skill int auto_increment; 修改数据类型

alter table interest change skill skill1 int; 修改字段名

alter table interest rename interest_1; 重命名表

"""

# ***************    表记录操作   ***************

"""


增：insert into stu(name) values("张");

删：delete from stu where score < 60;

改：select * from stu where score < 60;

查：update stu set name = '张' where id = 3;


"""

# ***************    范围比较    ***************

"""

in(), not in(), between val1 and val2 

select name,score from stu where score between 0 and 59;

select name,score from stu where class in ("AID12","AID13");

"""

# ***************    空值比较、分页    ***************

"""

is NULL , is not NULL

order by desc / asc

limit n : 显示前n条
limit m,n : 从第m+1条开始，显示n条

分页：每页10条，显示第6页内容
limit (61-)*10,10

"""

# ***************    MySQL普通查询   ***************

"""

3、select ...聚合函数 from 表名
1、where ...
2、group by ...
4、having ...
5、order by ...
6、limit ...;

"""

# ***************    聚合函数   ***************

"""

| 方法          | 功能                 |
| ------------- | -------------------- |
| avg(字段名)   | 该字段的平均值       |
| max(字段名)   | 该字段的最大值       |
| min(字段名)   | 该字段的最小值       |
| sum(字段名)   | 该字段所有记录的和   |
| count(字段名) | 统计该字段记录的个数 |

# 空值NULL不会被统计


having语句通常与group by联合使用 过滤由group by语句返回的记录集

where只能操作表中实际存在的字段,having操作的是聚合函数生成的显示列

"""

# ***************    索引  普通(MUL) and 唯一(UNI)    ***************

"""

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

# ***************    主键   ***************

"""

1、只能有一个主键字段 
2、所带约束 ：不允许重复,且不能为NULL 
3、KEY标志 ：PRI 
4、通常设置记录编号字段id,能唯一锁定一条记录


创建表添加主键

create table student(
id int auto_increment,
name varchar(20),
primary key(id)
)charset=utf8,auto_increment=10000;##设置自增长起始值

已有表添加主键
alter table 表名 add primary key(id);

删除主键索引
alter table 表名 drop primary key;

"""

# ***************    外键 foreign key   ***************

"""
foreign key(参考字段名) 
references 主表(被参考字段名) 
on delete 级联动作 
on update 级联动作

级联动作:
cascade •数据级联删除、更新(参考字段) 
restrict(默认) •从表有相关联记录,不允许主表操作 
set null •主表删除、更新,从表相关联记录字段值为NULL

eg:

创建主表master
create table master(
id int primary key auto_increment, 
name varchar(20),
class char(7),
money decimal(10,2)
) charset=utf8;


创建从表slave 设置外键 
create table slave(
stu_id int,name varchar(20), 
money decimal(10,2), 
foreign key(stu_id) references master(id) 
on delete cascade 
on update cascade
) charset=utf8;


insert into slave values(1,'唐伯虎',300),(2,'点秋香',300),(3,'祝枝山',300);

删除外键
alter table 表名 drop foreign key 外键名;

"""

# ***************    嵌套子查询   ***************

"""
把内层的查询结果作为外层的查询条件

eg:
把攻击值小于平均攻击值的英雄名字和攻击值显示出来
select name,attack from sanguo 
where attack < (select avg(attack) from sanguo);

eg:
找出每个国家攻击力最高的英雄的名字和攻击值
select name,attack,country from sanguo 
where (country,attack) in (select country, max(attack) from sanguo group by country);

"""

# ***************    多表查询  效率低  ***************

"""

笛卡尔积
select 字段名列表 from 表名列表;

多表查询
select 字段名列表 from 表名列表 where 条件;


select p.pname, c.cname from province p, city c where p.pid = c.cp_id;


select p.pname,c.cname,co.coname from province p, city c, county co where p.pid = c.cp_id and co.copid = c.cid;

"""

# ***************    连接查询  效率高 ***************

"""

内连接  inner join
显示匹配成功的结果  效果同多表查询

语法：
select 字段名 from 表1 
inner/left/right join 表2 on 条件 
inner/left/right join 表3 on 条件;

select p.pname,c.cname 
from province p 
inner join city c on p.pid = c.cp_id;

select p.pname,c.cname,co.coname 
from province p 
inner join city c on p.pid = c.cp_id 
inner join county co on c.cid = co.copid;


外连接
左外连接 left join

右外连接 right join


"""

# ***************  锁 （自动加锁和释放锁） ***************

"""
读锁：共享锁          加锁后别人能查 不能改

写锁：互斥锁/排它锁    加锁后别人不能查 不能改

颗粒度细分
表级锁：myisam
行级锁：innodb


"""










