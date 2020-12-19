"""

- **3、操作题**

综述：两张表，一张顾客信息表customers，一张订单表orders

表1：顾客信息表，完成后插入3条表记录

```mysql
c_id 类型为整型，设置为主键，并设置为自增长属性
c_name 字符类型，变长，宽度为20
c_age 微小整型，取值范围为0~255(无符号)
c_sex 枚举类型，要求只能在('M','F')中选择一个值
c_city 字符类型，变长，宽度为20
c_salary 浮点类型，要求整数部分最大为10位，小数部分为2位
```

create table customers ( c_id int primary key auto_increment,
c_name varchar(20),
c_age tinyint,
c_sex enum('M','F'),
c_city varchar(20),
c_salary decimal(12,1)
);

insert into customers values(1,'赵',19, 'M', '江苏', 11290.00),
(2,'钱',29, 'M', '上海', 21290.00),
(3,'sun',39, 'F', '北京', 31290.00);

表2：顾客订单表（在表中插入5条记录）

```mysql
o_id 整型
o_name 字符类型，变长，宽度为30
o_price 浮点类型，整数最大为10位，小数部分为2位
设置此表中的o_id字段为customers表中c_id字段的外键,更新删除同步
insert into orders values(1,"iphone",5288),(1,"ipad",3299),(3,"mate9",3688),(2,"iwatch",2222),(2,"r11",4400);
```

create table orders (o_id int,
o_name varchar(30),
o_price decimal(12,2),
foreign key(o_id) references customers(c_id)
on update cascade
on delete cascade);

insert into orders values(1,'赵', 290.00),
(1,'赵', 190.00),
(2,'钱', 490.00),
(1,'赵', 590.00),
(3,'sun', 70.00);


增删改查题

```mysql
1、返回customers表中，工资大于4000元，或者年龄小于29岁，满足这样条件的前2条记录
select * from customers c where c.c_salary > 4000 or c.c_age < 29 limit 2;

2、把customers表中，年龄大于等于25岁，并且地址是北京或者上海，这样的人的工资上调15%
update customers set c_salary=c_salary*1.15 where c_age >= 25 and (c_city = '北京' or c_city ='上海');

3、把customers表中，城市为北京的顾客，按照工资降序排列，并且只返回结果中的第一条记录
select * from customers where c_city='北京' order by c_salary desc limit 1;

4、选择工资c_salary最少的顾客的信息
select * from customers where c_salary = (select min(c_salary) from customers);

5、找到工资大于5000的顾客都买过哪些产品的记录明细
select o.o_id,o.o_name,o.o_price from orders o left join customers c on o.o_id = c.c_id where c.c_salary>15000 ;

6、删除外键限制
alter table orders drop foreign key "";

7、删除customers主键限制
alter table customers drop primary key;

8、增加customers主键限制c_id
alter table customers add primary key(c_id);

```







"""