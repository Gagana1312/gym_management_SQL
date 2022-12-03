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


select * from staff;
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

INSERT INTO marino.activity VALUES ('17001', 'Soccer', '41'),
('17002', 'Cricket', '42'),
('17003', 'Tennis', '43'),
('17004', 'Squash', '44'),
 ('17005', 'disc golf', '46');

-- Error Code: 1452. Cannot add or update a chxild row: a foreign key constraint fails (`marino`.`equiment`, CONSTRAINT `idactivity_fk_equipment` FOREIGN KEY (`idactivity`) REFERENCES `activity` (`idactivity`) ON DELETE CASCADE ON UPDATE RESTRICT)
  SET FOREIGN_KEY_CHECKS=0;
  SELECT @@GLOBAL.foreign_key_checks, @@SESSION.foreign_key_checks;
  -- SET VARIABLES LIKE 'FOREIGN_KEY_CHECKS';
