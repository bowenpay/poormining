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