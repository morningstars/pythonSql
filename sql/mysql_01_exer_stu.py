"""

create table students( id int primary key auto_increment,  name varchar(70) )charset = utf8;

在标中插入10万条数据

批量插入数据使用executemany方法 减少io操作 极大提升效率
executemany(sql,[data1,data2,data3])

建立索引
create index name on students(name);



"""

import pymysql

#
db = pymysql.connect(
    database='country',
    host='localhost',
    user='root',
    password='',
    port=3306,
    charset='utf8',
    table='students'
)

cur = db.cursor()


def close_db():
    cur.close()
    db.close()


# 一条sql语句对应一个io操作  效率低
def insert():
    for i in range(1, 1000000):
        # print(i,"name%s"%i)
        sql = "insert into students values('%s','%s');" % (i, "name%s" % i)
        try:
            cur.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)
            return False


# n条sql语句对应一个io操作  效率高
def insert2():
    data_list = []
    for i in range(1000000, 2000001):
        name = 'name{}'.format(str(i))
        # print(name)
        data_list.append((i, name))

    sql = "insert into students(id, name) values(%s,%s);"
    try:
        cur.executemany(sql, data_list)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
        return False


def delete():
    sql = "delete from students where id > 999999;"
    try:
        cur.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
        return False


if __name__ == '__main__':
    print("hello world")

    insert2()
    # data.delete()




"""

select user_id, count(user_id) cu from comment c group by user_id order by cu desc limit 10;

"""
