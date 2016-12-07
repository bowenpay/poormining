-- 给原表增加 下一年是否贫困、下一年年收入、下一年人均年收入 字段
alter table `yunnan_all_pinkunhu_2014`
ADD COLUMN  `ny_is_poor` int(11) DEFAULT 0,
ADD COLUMN  `ny_total_income` double DEFAULT -1,
ADD COLUMN  `ny_person_income` double DEFAULT -1;

alter table `yunnan_all_pinkunhu_2015`
ADD COLUMN  `ny_is_poor` int(11) DEFAULT 0,
ADD COLUMN  `ny_total_income` double DEFAULT -1,
ADD COLUMN  `ny_person_income` double DEFAULT -1;


alter table `yunnan_all_pinkunhu_2016`
ADD COLUMN  `ny_is_poor` int(11) DEFAULT 0,
ADD COLUMN  `ny_total_income` double DEFAULT -1,
ADD COLUMN  `ny_person_income` double DEFAULT -1;

-- TODO: 执行 `PYTHONPATH=. python data/dbutil.py` 以更新上面3个字段的信息

-- 新建开源用的数据库

CREATE DATABASE `poormining` CHARACTER SET utf8;

-- 填充2个县的数据

CREATE TABLE poormining.yunnan_all_pinkunhu_2014
AS
SELECT * FROM data_fupin.yunnan_all_pinkunhu_2014 where county='镇雄县' or county ='彝良县';

CREATE TABLE poormining.yunnan_all_pinkunhu_2015
AS
SELECT * FROM data_fupin.yunnan_all_pinkunhu_2015 where county='镇雄县' or county ='彝良县'

CREATE TABLE poormining.yunnan_all_pinkunhu_2016
AS
SELECT * FROM data_fupin.yunnan_all_pinkunhu_2016 where county='镇雄县' or county ='彝良县'

-- 去除秘密字段
update `yunnan_all_pinkunhu_2014` set `name` = concat(left(`name`, 1), '**'), `bank_number` = concat(left(`bank_number`, 6), '******'),`call_number` = concat(left(`call_number`, 3), '********'),`card_number` = '', `province`='', `city`='', `town`='', `village`='', `group`='';
update `yunnan_all_pinkunhu_2015` set `name` = concat(left(`name`, 1), '**'), `bank_number` = concat(left(`bank_number`, 6), '******'),`call_number` = concat(left(`call_number`, 3), '********'),`card_number` = '', `province`='', `city`='', `town`='', `village`='', `group`='';
update `yunnan_all_pinkunhu_2016` set `name` = concat(left(`name`, 1), '**'), `bank_number` = concat(left(`bank_number`, 6), '******'),`call_number` = concat(left(`call_number`, 3), '********'),`card_number` = '', `province`='', `city`='', `town`='', `village`='', `group`='';





