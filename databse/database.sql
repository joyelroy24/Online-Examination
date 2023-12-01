/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - online_examination_system
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`online_examination_system` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `online_examination_system`;

/*Table structure for table `answers` */

DROP TABLE IF EXISTS `answers`;

CREATE TABLE `answers` (
  `answer_id` int(11) NOT NULL AUTO_INCREMENT,
  `qstansr_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `mark_awarded` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`answer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `answers` */

insert  into `answers`(`answer_id`,`qstansr_id`,`student_id`,`mark_awarded`) values (1,1,6,'2'),(2,3,6,'2'),(3,3,6,'0');

/*Table structure for table `courses` */

DROP TABLE IF EXISTS `courses`;

CREATE TABLE `courses` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `courses` */

insert  into `courses`(`course_id`,`course_name`) values (7,'bsc computer'),(8,'BSC PHYSICS');

/*Table structure for table `examiner` */

DROP TABLE IF EXISTS `examiner`;

CREATE TABLE `examiner` (
  `examiner_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`examiner_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `examiner` */

insert  into `examiner`(`examiner_id`,`login_id`,`first_name`,`last_name`,`qualification`,`phone`,`email`) values (3,17,'SWAPNA','SUMAN','MCA','83666','S@gamil.com'),(6,20,'NITHYA','MS','MCA','8377','nithya@gmail.com');

/*Table structure for table `exams` */

DROP TABLE IF EXISTS `exams`;

CREATE TABLE `exams` (
  `exam_id` int(11) NOT NULL AUTO_INCREMENT,
  `exam_title` varchar(50) DEFAULT NULL,
  `exam_details` varchar(50) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `examiner_id` int(11) DEFAULT NULL,
  `exam_date` varchar(50) DEFAULT NULL,
  `exam_fees` varchar(50) DEFAULT NULL,
  `exam_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`exam_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `exams` */

insert  into `exams`(`exam_id`,`exam_title`,`exam_details`,`subject_id`,`examiner_id`,`exam_date`,`exam_fees`,`exam_status`) values (1,'python','OOP concepts',3,6,'2021-09-15','600','result published'),(4,'PYTHON','DATA TYPES',3,3,'2021-09-24','700','Announced'),(5,'GRAVITATIONAL FORCE','THEORIES ABOUT GRAVITITY',8,6,'2021-09-16','600','result published');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`user_name`,`password`,`user_type`) values (1,'admin','admin','admin'),(14,'','','examiner'),(13,'','','examiner'),(12,'','','examiner'),(11,'roy','roy','parent'),(7,'aa','aa','parent'),(8,'aa','bb','parent'),(9,'designer','aa','parent'),(10,'','','parent'),(15,'','','examiner'),(20,'nithya','nithya','examiner'),(17,'swapna','swapna','examiner'),(21,'hh','hh','parent'),(22,'kk','kk','parent'),(27,'joyel','joyel','student'),(26,'manu','manu','student'),(28,'henna','henna','student');

/*Table structure for table `parents` */

DROP TABLE IF EXISTS `parents`;

CREATE TABLE `parents` (
  `parent_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `house_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`parent_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `parents` */

insert  into `parents`(`parent_id`,`login_id`,`first_name`,`last_name`,`dob`,`phone`,`email`,`house_name`,`place`,`pincode`) values (1,9,'Sreya','Ks','','7594869862','sreyasajan175@gmail.com','Kariyezhath(h) p.o.perinjanam..thrissur','','12345'),(3,11,'ROY','KS','2021-09-01','7594869862','roy@gmail.com','KATTUKANDATHIL','PUTHUVYPPU','12345');

/*Table structure for table `participation` */

DROP TABLE IF EXISTS `participation`;

CREATE TABLE `participation` (
  `participation_id` int(11) NOT NULL AUTO_INCREMENT,
  `exam_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`participation_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `participation` */

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `exam_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`exam_id`,`student_id`,`amount`) values (1,5,7,'600'),(2,4,6,'700'),(3,4,5,'700'),(4,1,6,'600');

/*Table structure for table `questionanswer` */

DROP TABLE IF EXISTS `questionanswer`;

CREATE TABLE `questionanswer` (
  `qstansr_id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) DEFAULT NULL,
  `option` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`qstansr_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `questionanswer` */

insert  into `questionanswer`(`qstansr_id`,`question_id`,`option`,`status`) values (1,1,'YES','true'),(2,1,'NO','false'),(3,2,'YES','true'),(4,2,'NO','false'),(5,3,'YES','true'),(6,3,'NO','false');

/*Table structure for table `questions` */

DROP TABLE IF EXISTS `questions`;

CREATE TABLE `questions` (
  `question_id` int(11) NOT NULL AUTO_INCREMENT,
  `exam_id` int(11) DEFAULT NULL,
  `question` varchar(50) DEFAULT NULL,
  `maximum_mark` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`question_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `questions` */

insert  into `questions`(`question_id`,`exam_id`,`question`,`maximum_mark`,`description`) values (1,4,'Is Python is Object Orineted ','2','easy'),(2,4,'Is Python is portable ','2','easy'),(3,4,'is python is interpreted','2','easy');

/*Table structure for table `result` */

DROP TABLE IF EXISTS `result`;

CREATE TABLE `result` (
  `result_id` int(11) NOT NULL AUTO_INCREMENT,
  `exam_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `total_mark` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`result_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `result` */

/*Table structure for table `students` */

DROP TABLE IF EXISTS `students`;

CREATE TABLE `students` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_id` int(11) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `students` */

insert  into `students`(`student_id`,`parent_id`,`login_id`,`course_id`,`first_name`,`last_name`,`dob`,`phone`,`email`) values (6,3,27,7,'JOYEL','KR','2017-02-14','7366278','J@gmail.com'),(5,3,26,7,'MANUEL','KR','2015-07-02','75948698','MANU@gmail.com'),(7,3,28,8,'HENNA','HELAN','2021-09-15','7594869862','henna@gmail.com');

/*Table structure for table `subjects` */

DROP TABLE IF EXISTS `subjects`;

CREATE TABLE `subjects` (
  `subject_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` int(11) DEFAULT NULL,
  `subject_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `subjects` */

insert  into `subjects`(`subject_id`,`course_id`,`subject_name`) values (3,7,'PYTHON'),(8,8,'PHYSICS');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
