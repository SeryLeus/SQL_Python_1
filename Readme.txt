1) Под admin зайти в CMD
2) `choco install mysql`
3) `mysql -uroot`
4) `show databases`
5) `create database shop`
6) `use shop`
7) `show tables`
8) `create table goods ( name varchar(255), price float );
9) `show tables`
10) `select * from goods`
11) `exit`
12) `mysql -uroot -D shop < insert_data.sql`
13) `mysql -uroot`
14) `use shop`
15) `select * from goods`


Run back-end:
python server.py

Run client:
http://127.0.0.1:5000/


