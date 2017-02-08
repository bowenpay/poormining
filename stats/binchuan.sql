

-- 新建开源用的数据库

CREATE DATABASE `binchuan_data` CHARACTER SET utf8;
USE `binchuan_data`;

---- 填充2个县的数据

-- 贫困户数据
CREATE TABLE binchuan_data.yunnan_all_pinkunhu_2014
AS
SELECT * FROM data_fupin.yunnan_all_pinkunhu_2014 where county='宾川县';

CREATE TABLE binchuan_data.yunnan_all_pinkunhu_2015
AS
SELECT * FROM data_fupin.yunnan_all_pinkunhu_2015 where county='宾川县';

CREATE TABLE binchuan_data.yunnan_all_pinkunhu_2016
AS
SELECT * FROM data_fupin.yunnan_all_pinkunhu_2016 where county='宾川县';

-- 删除特定字段
ALTER TABLE binchuan_data.yunnan_all_pinkunhu_2014 DROP `help_plan`, DROP `other_reason`, DROP `sid`, DROP `avatar`;
ALTER TABLE binchuan_data.yunnan_all_pinkunhu_2015 DROP `help_plan`, DROP `other_reason`, DROP `sid`, DROP `avatar`;
ALTER TABLE binchuan_data.yunnan_all_pinkunhu_2016 DROP `help_plan`, DROP `other_reason`, DROP `sid`, DROP `avatar`;


ALTER TABLE binchuan_data.yunnan_all_pinkunhu_2014 DROP `ny_is_poor`, DROP `ny_total_income`, DROP `ny_person_income`;
ALTER TABLE binchuan_data.yunnan_all_pinkunhu_2015 DROP `ny_is_poor`, DROP `ny_total_income`, DROP `ny_person_income`;
ALTER TABLE binchuan_data.yunnan_all_pinkunhu_2016 DROP `ny_is_poor`, DROP `ny_total_income`, DROP `ny_person_income`;

-- 加密秘密字段
update `binchuan_data`.`yunnan_all_pinkunhu_2014` set `card_number` = md5(`card_number`), `call_number` = md5(`call_number`);
update `binchuan_data`.`yunnan_all_pinkunhu_2015` set `card_number` = md5(`card_number`), `call_number` = md5(`call_number`);
update `binchuan_data`.`yunnan_all_pinkunhu_2016` set `card_number` = md5(`card_number`), `call_number` = md5(`call_number`);


-- 贫困家庭数据
CREATE TABLE binchuan_data.yunnan_all_pinkunjiating_2014
AS
SELECT * FROM data_fupin.yunnan_all_pinkunjiating_2014 where county='宾川县';

CREATE TABLE binchuan_data.yunnan_all_pinkunjiating_2015
AS
SELECT * FROM data_fupin.yunnan_all_pinkunjiating_2015 where county='宾川县';

CREATE TABLE binchuan_data.yunnan_all_pinkunjiating_2016
AS
SELECT * FROM data_fupin.yunnan_all_pinkunjiating_2016 where county='宾川县';


-- 删除特定字段
ALTER TABLE binchuan_data.yunnan_all_pinkunjiating_2014 DROP `change_reason`, DROP `change_type`, DROP `fuchi_fangshi`, DROP `sid`;
ALTER TABLE binchuan_data.yunnan_all_pinkunjiating_2015 DROP `change_reason`, DROP `change_type`, DROP `fuchi_fangshi`, DROP `sid`;
ALTER TABLE binchuan_data.yunnan_all_pinkunjiating_2016 DROP `change_reason`, DROP `change_type`, DROP `fuchi_fangshi`, DROP `sid`;

-- 加密秘密字段
update `binchuan_data`.`yunnan_all_pinkunjiating_2014` set `card_number` = md5(`card_number`), `member_card_number` = md5(`member_card_number`);
update `binchuan_data`.`yunnan_all_pinkunjiating_2015` set `card_number` = md5(`card_number`), `member_card_number` = md5(`member_card_number`);
update `binchuan_data`.`yunnan_all_pinkunjiating_2016` set `card_number` = md5(`card_number`), `member_card_number` = md5(`member_card_number`);
