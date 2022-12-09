-- DROP DATABASE marino;
CREATE DATABASE  IF NOT EXISTS marino;
USE marino;


DROP TABLE IF EXISTS user;

CREATE TABLE user (
  userid int NOT NULL auto_increment,
  first_name varchar(45) NOT NULL,
  last_name varchar(45) NOT NULL,
  age varchar(45) DEFAULT NULL,
  phone_number varchar(45) DEFAULT NULL,
  emailid varchar(45) NOT NULL,
  password varchar(45) NOT NULL,
  PRIMARY KEY (userid)
);


-- DROP TABLE IF EXISTS trainer;
-- CREATE TABLE trainer (
--   idtrainer int NOT NULL auto_increment,
--   Name varchar(45) NOT NULL,
--   age int NOT NULL,
--   phone_number int NOT NULL,
--   emailid varchar(45) NOT NULL,
--   password varchar(45) NOT NULL,
--   PRIMARY KEY (idtrainer)
-- );



DROP TABLE IF EXISTS staff;
CREATE TABLE staff (
  idstaff int NOT NULL auto_increment,
  staff_name varchar(45) NOT NULL,
  staff_age int NOT NULL,
  phone_number int NOT NULL,
  emailid varchar(45) NOT NULL,
  password varchar(45) NOT NULL,
  PRIMARY KEY (idstaff)
) ;


DROP TABLE IF EXISTS payment;

CREATE TABLE payment (
  idpayment int NOT NULL auto_increment,
  date date DEFAULT NULL,
  amount int DEFAULT NULL,
  no_of_activities int DEFAULT NULL,
  user_id int DEFAULT NULL,
  PRIMARY KEY (idpayment),
  CONSTRAINT user_id
  FOREIGN KEY (user_id) 
  REFERENCES user (userid)
  on update restrict on delete cascade
) ;



DROP TABLE IF EXISTS locker;

CREATE TABLE locker (
  idlocker int NOT NULL auto_increment,
  type_of_locker varchar(45) NOT NULL,
  idstaff int NOT NULL,
  userid int NOT NULL,
  PRIMARY KEY (idlocker),
  KEY userid_idx (userid),
  KEY idstaff_idx (idstaff),
  CONSTRAINT idstaff
  FOREIGN KEY (idstaff)
  REFERENCES staff (idstaff)
  on update restrict on delete cascade,
  CONSTRAINT userid 
  FOREIGN KEY (userid)
  REFERENCES user (userid)
  on update restrict on delete cascade
);

DROP TABLE IF EXISTS activity;

CREATE TABLE activity (
  idactivity int NOT NULL auto_increment,
  name varchar(45) NOT NULL,
  room_no int NOT NULL,
  price INT NOT NULL,
  -- duration time NOT NULL,
--   date date NOT NULL,
  -- idtrainer int NOT NULL,
 --  user_id int NOT NULL,
  PRIMARY KEY (idactivity)
  -- CONSTRAINT idtrainer
  -- FOREIGN KEY (idtrainer)
  -- References trainer (idtrainer)
  -- on update restrict on delete cascade,
 --  CONSTRAINT userid_fk_activity 
--   FOREIGN KEY (user_id)
--   REFERENCES user (userid)
--   on update restrict on delete cascade
  );



DROP TABLE IF EXISTS equipment;

CREATE TABLE equipment (
  idequipment int NOT NULL auto_increment,
  name varchar(45) NOT NULL,
  idstaff int NOT NULL,
  idactivity int NOT NULL,
  PRIMARY KEY (idequipment),
  CONSTRAINT idstaff_fk_equipment
  FOREIGN KEY (idstaff)
  references staff (idstaff),
  -- on update restrict on delete cascade,
  CONSTRAINT idactivity_fk_equipment
  FOREIGN KEY (idactivity)
  References activity (idactivity)
  -- on update restrict on delete cascade
);


DROP TABLE IF EXISTS Admin;

CREATE TABLE Admin (
  emailid varchar(45) NOT NULL,
  password varchar(45) NOT NULL,
  PRIMARY KEY (emailid)
);

CREATE TABLE payment (
  idpayment int NOT NULL auto_increment,
  idactivity INT NOT NULL,
  userid INT NOT NULL,
  PRIMARY KEY (idpayment)
);


INSERT INTO Admin VALUES 
('Arpan@gmail.com','arpan'),
('gagana@gmail.com','gagana');

INSERT INTO marino.staff VALUES ('601', 'Gagana A', '23', '980637282', 'gagana@gmail.com', 'gags#12345'),
 ('602', 'Wennie', '24', '986745382', 'wen@gmail.com', 'wen#12345'),
('603', 'Kiara', '25', '874827364', 'kiara@gmail.com', 'kiara#12345'),
('604','Neha', '23', '89983766', 'neha@gmail.com', 'neha#12345');

SELECT * from staff;
SELECT * from user;

INSERT INTO marino.user
VALUES ('001', 'Arpan', 'Patel', '23', '7861319272', 'arpan@yahoo.com', 'arpan@12345'),
('002', 'Jin', 'Kim', '29', '7869462738', 'jin@gmail.com', 'jin@12345'),
('003', 'Hope', 'Mikalson', '19', '7289462782', 'hope@gmail.com', 'hope@12345');


SELECT * from activity;
DELETE FROM staff WHERE emailid = 'testing@gmail.com';


-- Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column.  To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.


 select * from payment;
select * from staff;
select * from user;
select * from admin;
select * from locker;
select * from equipment;
-- drop table locker;
INSERT INTO marino.locker VALUES ('901', 'Standard', '603', '3'),
('902', 'Personal', '601', '2'),('903', '2-tier', '602', '1');

INSERT INTO marino.equipment VALUES ('1101', 'soccer ball.', '603', '17001'),
('1102', 'Flying disc', '601', '17005'),('1103', 'Racquets', '601', '17003')
,('1104', 'Nets', '601', '17003'),('1105', 'Sticks', '602', '17006'),
('1106', 'Bats', '601', '17002');

-- INSERT INTO marino.activity VALUES ('17001', 'Soccer', '41',200),
-- ('17002', 'Cricket', '42',400),
-- ('17003', 'Tennis', '43',300),
-- ('17004', 'Squash', '44',250),
--  ('17005', 'disc golf', '46',430);

-- -- Error Code: 1452. Cannot add or update a chxild row: a foreign key constraint fails (`marino`.`equiment`, CONSTRAINT `idactivity_fk_equipment` FOREIGN KEY (`idactivity`) REFERENCES `activity` (`idactivity`) ON DELETE CASCADE ON UPDATE RESTRICT)
--   SET FOREIGN_KEY_CHECKS=0;
--   SELECT @@GLOBAL.foreign_key_checks, @@SESSION.foreign_key_checks;
--   -- SET VARIABLES LIKE 'FOREIGN_KEY_CHECKS';
--   
--   SELECT * FROM activity;
--   SELECT * from equipment;
--   
--   SELECT * from activity as a , equipment as e where a.idactivity=e.idactivity;
--   
--   SELECT a.idactivity,a.name,a.room_no,e.idequipment,e.name from activity as a JOIN equipment as e ON a.idactivity=e.idactivity;

-- INSERT INTO marino.trainer VALUES ('301', 'Chris', '25', '784637380', 'chris@gmail.com', 'chris'),
-- ('302', 'Felix', '24', '23432546', 'felix@gmail.com', 'felix'),
-- ('303', 'Alex', '25', '33452878', 'alex@gmail.com', 'alex');


-- INSERT INTO marino.payment  VALUES ('101001', '17003', '3'), ('101002', '17003', '2')
--  ,('101003', '17002', '3'),('101004', '17001', '1'), ('101005', '17002', '3'), ('101006', '17004', '4');
--  
-- select p.idpayment,a.price,a.idactivity,a.name,u.userid,u.first_name from payment as p JOIN activity as a ON p.idactivity=a.idactivity JOIN user as u ON p.userid=u.userid;


-- delimiter //
-- create procedure staff_reg(IN staff_name varchar(40),IN staff_age int, 
-- IN phone_number VARCHAR(10),IN emailid varchar(46), IN password varchar(40) )
-- begin
-- insert into marino.staff(staff_name,staff_age,phone_number,emailid,password) 
-- values(staff_name,staff_age,phone_number,emailid,password);
-- end
-- //
--    
-- call staff_reg('Chris',24,675672876,'chris@gmail.com','chris');

-- delimiter $$
-- create procedure user_reg(IN first_name varchar(40),IN last_name varchar(40),IN age int, 
-- IN phone_number VARCHAR(10),IN emailid varchar(46), IN password varchar(40) )
-- begin
-- insert into marino.user(first_name,last_name,age,phone_number,emailid,password) 
--  values(first_name,last_name,age,phone_number,emailid,password);
-- end
-- $$
--    
-- call user_reg('Chris','Jane',24,675672876,'chris@gmail.com','chris');

-- delimiter $$
-- create procedure staff_del(IN email_id varchar(46), IN pwd varchar(40) )
-- begin
-- delete from staff WHERE emailid = email_id AND password = pwd;
-- end
-- $$

-- -- SET SQL_SAFE_UPDATES = 0;

-- call staff_del('chris@gmail.com','chris');

-- delimiter $$
-- create procedure user_del(IN email_id varchar(46), IN pwd varchar(40) )
-- begin
-- delete from user WHERE emailid = email_id AND password = pwd;
-- end
-- $$

-- delimiter $$
-- create procedure locker_reg(IN type_of_locker varchar(40),IN idstaff int, IN userid int )
-- begin
-- insert into marino.locker(type_of_locker,idstaff,userid) 
-- values(type_of_locker,idstaff,0);
-- end
-- $$
-- --    
-- call locker_reg('standard',608,4);

-- delimiter $$
-- create procedure locker_del(IN id_locker INT )
-- begin
-- Delete from locker where idlocker = id_locker;
-- end
-- $$

call locker_del(908);

-- delimiter $$
--  create procedure equipment_reg(IN name varchar(40),IN idstaff int,IN idactivity INT )
--    begin
--    Insert into marino.equipment(name,idstaff,idactivity) values(name,idstaff,idactivity);
--    end
--    $$
   
call equipment_reg('hockey stick',604,17006);

-- delimiter $$
-- create procedure equipment_del(IN id_equipment INT )
-- begin
-- Delete from equipment where idequipment = id_equipment;
-- end
-- $$

-- call equipment_del(904);
 
-- DROp procedure is exists activity_reg(name_,room_no,price_);

-- delimiter $$
-- create procedure activity_reg(IN name_ varchar(40),IN room_no_ int,IN price_ int )
-- begin
-- Insert into marino.activity (name,room_no,price) values (name_,room_no_,price_);
-- end
-- $$
   
call activity_reg('foosball',92,10);


select p.idpayment,a.price,a.idactivity,a.name,u.userid,u.first_name 
from payment as p JOIN activity as a ON p.idactivity=a.idactivity JOIN user as u ON p.userid=u.userid where u.userid=3
GROUP BY p.idpayment ;


delimiter $$
create procedure activity_del(IN id_activity INT )
begin
Delete from activity where idactivity = id_activity;
end
$$
call activity_del(17006);

-- delimiter $$
-- create procedure activity_Equip_table()
-- begin
-- SELECT a.idactivity,a.name,a.room_no,e.idequipment,e.name 
-- from activity as a JOIN equipment as e ON a.idactivity=e.idactivity;
-- end
-- $$
   
-- call activity_Equip_table()

-- delimiter $$
-- create procedure payment_del(in idactivity_ int)
-- begin
-- DELETE FROM payment where idactivity=idactivity_;
-- end
-- $$

DROP PROCEDURE IF EXISTS user_activity;

delimiter $$
create procedure user_activity(IN idactivity_ int, IN userid_ INT)
begin
Insert into payment(idactivity,userid) values (idactivity_,userid_);
end
$$

call user_activity(17001,1);
select* from payment;

DROP FUNCTION IF EXISTS marino.totalPayment;

 DELIMITER //
 CREATE FUNCTION totalPayment(id INT)
 RETURNS INT
DETERMINISTIC READS SQL DATA 
BEGIN
  DECLARE total_payment INT;
select SUM(a.price)
into total_payment
from payment as p JOIN activity as a ON p.idactivity=a.idactivity 
JOIN user as u ON p.userid=u.userid where u.userid = id;
  RETURN(total_payment);
END//


SELECT  totalPayment(3) from payment LIMIT 1;


