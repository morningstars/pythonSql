

"""
**创建库 ：country（指定字符编码为utf8）**
create database country charset utf8;

**创建表 ：sanguo 字段：id 、name、attack、defense、gender、country**
create table sanguo(id int primary key auto_increment,
                    name varchar(30),
                    attack float, defense float,
                    gender varchar(5),
                    country varchar(10));

**插入5条表记录（id 1-5,name-诸葛亮、司马懿、貂蝉、张飞、赵云），攻击>100,防御<100）**
insert into sanguo values(1,'诸葛亮',90,90,'男', '蜀国') ,
                            (2,'司马懿',90,90,'男', '魏国'),
                            (3,'貂蝉',90,90,'女', '群雄'),
                            (4,'张飞',90,90,'男', '蜀国'),
                            (5,'赵云',90,90,'男', '蜀国');

**查找所有蜀国人的信息**
select * from sanguo where country = "蜀国";

**将赵云的攻击力设置为360,防御力设置为68**
update sanguo set attack=360, defense=68 where name = '赵云';

**将吴国英雄中攻击值为110的英雄的攻击值改为100,防御力改为60**
update sanguo set attack=100,defense=60 where attack=110 and country='吴国';

**找出攻击值高于200的蜀国英雄的名字、攻击力**
select name,attack from sanguo where attack>200 and country="蜀国";

**将蜀国英雄按攻击值从高到低排序**
select * from sanguo where country="蜀国" order by attack desc;

**魏蜀两国英雄中名字为三个字的按防御值升序排列**
select * from sanguo where country in ("蜀国","魏国") and name like '___' order by defense asc;

**在蜀国英雄中,查找攻击值前3名且名字不为 NULL 的英雄的姓名、攻击值和国家**
select name,attack,country from sanguo where country="蜀国" and name is not null order by attack desc limit 3;
"""