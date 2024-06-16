/*
SQLyog Enterprise - MySQL GUI v8.02 RC
MySQL - 5.5.5-10.4.17-MariaDB : Database - punit
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`punit` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `punit`;

/*Table structure for table `admindata` */

DROP TABLE IF EXISTS `admindata`;

CREATE TABLE `admindata` (
  `name` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `admindata` */

insert  into `admindata`(`name`,`address`,`contact`,`email`) values ('Mayank Sharma','Ramganj Mandi','9785385474','b@gmail.com'),('Daksh jain','kota','7896541230','p@gmail.com'),('Punit sharma','near govt hopital','9529676199','sagar@gamail.com');

/*Table structure for table `doctor_data` */

DROP TABLE IF EXISTS `doctor_data`;

CREATE TABLE `doctor_data` (
  `name` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `speciality` varchar(100) DEFAULT NULL,
  `current_hospital` varchar(100) DEFAULT NULL,
  `work_experience` varchar(100) DEFAULT NULL,
  `mon` varchar(100) DEFAULT NULL,
  `tues` varchar(100) DEFAULT NULL,
  `wed` varchar(100) DEFAULT NULL,
  `thu` varchar(100) DEFAULT NULL,
  `fri` varchar(100) DEFAULT NULL,
  `sat` varchar(100) DEFAULT NULL,
  `sun` varchar(100) DEFAULT NULL,
  `timing` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `doctor_id` int(11) NOT NULL AUTO_INCREMENT,
  `email_of_hospital` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

/*Data for the table `doctor_data` */

insert  into `doctor_data`(`name`,`address`,`contact`,`speciality`,`current_hospital`,`work_experience`,`mon`,`tues`,`wed`,`thu`,`fri`,`sat`,`sun`,`timing`,`email`,`doctor_id`,`email_of_hospital`) values ('PUNIT SHARMA','near govt hopital','9785385474','Cardiologist','maitri','8','no','yes','no','yes','no','yes','no','9am to 6pm','a@gmail.com',3,'o@gmail.com'),('Madhur','near govt hopital','9529676199','Cardiovascular Surgeon','maitri','7','no','yes','no','yes','no','yes','no','9am to 6pm','g@gmail.com',4,'o@gmail.com'),('Punit sharma','near govt hopital','9529676199','Dentist','sudha','6','yes','no','yes','no','yes','no','no','9am to 6pm','y@gmail.com',5,'r@gmail.com'),('Riddhi chohan','Talwandi circle kota','7014212844','Emergency Doctors','gyan shati','2 years','yes','yes','yes','yes','yes','yes','no','11:30AM to 12:30PM','r@gmail.com',6,'m@gmail.com'),('vikram singh Rathore','Dadabari kota','8001214544','ENT Specialist','sudha','4 Years','yes','yes','yes','yes','yes','no','no','2.00PM to 4.00PM','v@gmail.com',7,'r@gmail.com'),('Abhisek sharma ','kesapura kota','70014212844','Gastroenterologist','kota heart','6','yes','yes','yes','yes','no','no','no','4.00PM to 6.00PM','a@gmail.com',8,'f@gmail.com');

/*Table structure for table `hospital_data` */

DROP TABLE IF EXISTS `hospital_data`;

CREATE TABLE `hospital_data` (
  `hname` varchar(100) DEFAULT NULL,
  `lno` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `emergency` varchar(100) DEFAULT NULL,
  `g_beds` varchar(100) DEFAULT NULL,
  `ac_beds` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `hospital_data` */

insert  into `hospital_data`(`hname`,`lno`,`address`,`contact`,`emergency`,`g_beds`,`ac_beds`,`email`) values ('kota heart','111','Near govt. hospital morak station','9529676199','Y','100','100','f@gmail.com'),('shanti hospital','1000','Bsnl circle kota,rajasthan','9785385474','Y','200','100','m@gmail.com'),('Matrii hospital','1008','commerce collage,kota','9829675188','N','100','100','o@gmail.com'),('sudha_Hospital','1003','kota','9829708354','Y','no','yes','r@gmail.com');

/*Table structure for table `logindata` */

DROP TABLE IF EXISTS `logindata`;

CREATE TABLE `logindata` (
  `email` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  `con_pass` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `logindata` */

insert  into `logindata`(`email`,`password`,`usertype`,`con_pass`) values ('b@gmail.com','2K','admin','2K'),('f@gmail.com','44','hospital','44'),('m@gmail.com','66','hospital','66'),('o@gmail.com','o','hospital','0'),('p@gmail.com','2','admin','2'),('r@gmail.com','r','hospital','r'),('sagar@gamail.com','100','admin','100');

/*Table structure for table `photodata` */

DROP TABLE IF EXISTS `photodata`;

CREATE TABLE `photodata` (
  `user_email` varchar(100) NOT NULL,
  `photo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `photodata` */

insert  into `photodata`(`user_email`,`photo`) values ('22','1711589382.jpg'),('55','1711675470.jpg'),('77','1711748270.jpg'),('88','1711152306.jpg'),('b@gmail.com','1711749109.jpg'),('f@gmail.com','1712012178.jpg'),('m@gmail.com','1712012711.jpg'),('o@gmail.com','1712830327.jpg'),('p@gmail.com','1711749146.jpg'),('r@gmail.com','1712012243.jpg'),('sagar@gamail.com','1712012490.jpg');

/*Table structure for table `hospital_with_photo` */

DROP TABLE IF EXISTS `hospital_with_photo`;

/*!50001 DROP VIEW IF EXISTS `hospital_with_photo` */;
/*!50001 DROP TABLE IF EXISTS `hospital_with_photo` */;

/*!50001 CREATE TABLE `hospital_with_photo` (
  `hname` varchar(100) DEFAULT NULL,
  `lno` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `emergency` varchar(100) DEFAULT NULL,
  `g_beds` varchar(100) DEFAULT NULL,
  `ac_beds` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `user_email` varchar(100) NOT NULL,
  `photo` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 */;

/*View structure for view hospital_with_photo */

/*!50001 DROP TABLE IF EXISTS `hospital_with_photo` */;
/*!50001 DROP VIEW IF EXISTS `hospital_with_photo` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `hospital_with_photo` AS (select `hospital_data`.`hname` AS `hname`,`hospital_data`.`lno` AS `lno`,`hospital_data`.`address` AS `address`,`hospital_data`.`contact` AS `contact`,`hospital_data`.`emergency` AS `emergency`,`hospital_data`.`g_beds` AS `g_beds`,`hospital_data`.`ac_beds` AS `ac_beds`,`hospital_data`.`email` AS `email`,`photodata`.`user_email` AS `user_email`,`photodata`.`photo` AS `photo` from (`hospital_data` join `photodata` on(`hospital_data`.`email` = `photodata`.`user_email`))) */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
