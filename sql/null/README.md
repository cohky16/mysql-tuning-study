nullのインデックスの確認

**before**

```
mysql> explain select * from test_database.users where name is null;
+----+-------------+-------+------------+------+---------------+------+---------+------+--------+----------+-------------+
| id | select_type | table | partitions | type | possible_keys | key  | key_len | ref  | rows   | filtered | Extra       |
+----+-------------+-------+------------+------+---------------+------+---------+------+--------+----------+-------------+
|  1 | SIMPLE      | users | NULL       | ALL  | NULL          | NULL | NULL    | NULL | 150000 |    10.00 | Using where |
+----+-------------+-------+------------+------+---------------+------+---------+------+--------+----------+-------------+
1 row in set, 1 warning (0.01 sec)
```

**after**

nullでもインデックスは効く

```
mysql> explain select * from test_database.users where name is null;
+----+-------------+-------+------------+------+---------------+------------+---------+-------+------+----------+-----------------------+
| id | select_type | table | partitions | type | possible_keys | key        | key_len | ref   | rows | filtered | Extra                 |
+----+-------------+-------+------------+------+---------------+------------+---------+-------+------+----------+-----------------------+
|  1 | SIMPLE      | users | NULL       | ref  | name_index    | name_index | 259     | const |    1 |   100.00 | Using index condition |
+----+-------------+-------+------------+------+---------------+------------+---------+-------+------+----------+-----------------------+
1 row in set, 1 warning (0.00 sec)
```