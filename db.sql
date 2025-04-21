/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - counterfeit
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`counterfeit` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `counterfeit`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add dataset_table',7,'add_dataset_table'),
(26,'Can change dataset_table',7,'change_dataset_table'),
(27,'Can delete dataset_table',7,'delete_dataset_table'),
(28,'Can view dataset_table',7,'view_dataset_table'),
(29,'Can add distributor_table',8,'add_distributor_table'),
(30,'Can change distributor_table',8,'change_distributor_table'),
(31,'Can delete distributor_table',8,'delete_distributor_table'),
(32,'Can view distributor_table',8,'view_distributor_table'),
(33,'Can add login_table',9,'add_login_table'),
(34,'Can change login_table',9,'change_login_table'),
(35,'Can delete login_table',9,'delete_login_table'),
(36,'Can view login_table',9,'view_login_table'),
(37,'Can add product_table',10,'add_product_table'),
(38,'Can change product_table',10,'change_product_table'),
(39,'Can delete product_table',10,'delete_product_table'),
(40,'Can view product_table',10,'view_product_table'),
(41,'Can add user_table',11,'add_user_table'),
(42,'Can change user_table',11,'change_user_table'),
(43,'Can delete user_table',11,'delete_user_table'),
(44,'Can view user_table',11,'view_user_table'),
(45,'Can add stock_table',12,'add_stock_table'),
(46,'Can change stock_table',12,'change_stock_table'),
(47,'Can delete stock_table',12,'delete_stock_table'),
(48,'Can view stock_table',12,'view_stock_table'),
(49,'Can add shop_table',13,'add_shop_table'),
(50,'Can change shop_table',13,'change_shop_table'),
(51,'Can delete shop_table',13,'delete_shop_table'),
(52,'Can view shop_table',13,'view_shop_table'),
(53,'Can add request_from_shop',14,'add_request_from_shop'),
(54,'Can change request_from_shop',14,'change_request_from_shop'),
(55,'Can delete request_from_shop',14,'delete_request_from_shop'),
(56,'Can view request_from_shop',14,'view_request_from_shop'),
(57,'Can add request_from_distributor',15,'add_request_from_distributor'),
(58,'Can change request_from_distributor',15,'change_request_from_distributor'),
(59,'Can delete request_from_distributor',15,'delete_request_from_distributor'),
(60,'Can view request_from_distributor',15,'view_request_from_distributor'),
(61,'Can add order_table',16,'add_order_table'),
(62,'Can change order_table',16,'change_order_table'),
(63,'Can delete order_table',16,'delete_order_table'),
(64,'Can view order_table',16,'view_order_table'),
(65,'Can add order_details',17,'add_order_details'),
(66,'Can change order_details',17,'change_order_details'),
(67,'Can delete order_details',17,'delete_order_details'),
(68,'Can view order_details',17,'view_order_details'),
(69,'Can add feedback_table',18,'add_feedback_table'),
(70,'Can change feedback_table',18,'change_feedback_table'),
(71,'Can delete feedback_table',18,'delete_feedback_table'),
(72,'Can view feedback_table',18,'view_feedback_table'),
(73,'Can add complaint_table',19,'add_complaint_table'),
(74,'Can change complaint_table',19,'change_complaint_table'),
(75,'Can delete complaint_table',19,'delete_complaint_table'),
(76,'Can view complaint_table',19,'view_complaint_table'),
(77,'Can add chatbot_table',20,'add_chatbot_table'),
(78,'Can change chatbot_table',20,'change_chatbot_table'),
(79,'Can delete chatbot_table',20,'delete_chatbot_table'),
(80,'Can view chatbot_table',20,'view_chatbot_table'),
(81,'Can add distributor_product_table',21,'add_distributor_product_table'),
(82,'Can change distributor_product_table',21,'change_distributor_product_table'),
(83,'Can delete distributor_product_table',21,'delete_distributor_product_table'),
(84,'Can view distributor_product_table',21,'view_distributor_product_table'),
(85,'Can add shop_product_table',22,'add_shop_product_table'),
(86,'Can change shop_product_table',22,'change_shop_product_table'),
(87,'Can delete shop_product_table',22,'delete_shop_product_table'),
(88,'Can view shop_product_table',22,'view_shop_product_table'),
(89,'Can add shop_bill_table',23,'add_shop_bill_table'),
(90,'Can change shop_bill_table',23,'change_shop_bill_table'),
(91,'Can delete shop_bill_table',23,'delete_shop_bill_table'),
(92,'Can view shop_bill_table',23,'view_shop_bill_table'),
(93,'Can add bill_table',24,'add_bill_table'),
(94,'Can change bill_table',24,'change_bill_table'),
(95,'Can delete bill_table',24,'delete_bill_table'),
(96,'Can view bill_table',24,'view_bill_table'),
(97,'Can add bil_details',25,'add_bil_details'),
(98,'Can change bil_details',25,'change_bil_details'),
(99,'Can delete bil_details',25,'delete_bil_details'),
(100,'Can view bil_details',25,'view_bil_details');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `c_app_bil_details` */

DROP TABLE IF EXISTS `c_app_bil_details`;

CREATE TABLE `c_app_bil_details` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `SHOP_PRODUCT_id` bigint NOT NULL,
  `BILL_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `C_App_bil_details_SHOP_PRODUCT_id_b61ab85f_fk_C_App_sho` (`SHOP_PRODUCT_id`),
  KEY `C_App_bil_details_BILL_id_1cd897be_fk_C_App_bill_table_id` (`BILL_id`),
  CONSTRAINT `C_App_bil_details_BILL_id_1cd897be_fk_C_App_bill_table_id` FOREIGN KEY (`BILL_id`) REFERENCES `c_app_bill_table` (`id`),
  CONSTRAINT `C_App_bil_details_SHOP_PRODUCT_id_b61ab85f_fk_C_App_sho` FOREIGN KEY (`SHOP_PRODUCT_id`) REFERENCES `c_app_shop_product_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `c_app_bil_details` */

/*Table structure for table `c_app_bill_table` */

DROP TABLE IF EXISTS `c_app_bill_table`;

CREATE TABLE `c_app_bill_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` double NOT NULL,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `SHOP_id` bigint NOT NULL,
  `phone` bigint NOT NULL,
  `user` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `C_App_bill_table_SHOP_id_5d71e405_fk_C_App_shop_table_id` (`SHOP_id`),
  CONSTRAINT `C_App_bill_table_SHOP_id_5d71e405_fk_C_App_shop_table_id` FOREIGN KEY (`SHOP_id`) REFERENCES `c_app_shop_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `c_app_bill_table` */

/*Table structure for table `c_app_chatbot_table` */

DROP TABLE IF EXISTS `c_app_chatbot_table`;

CREATE TABLE `c_app_chatbot_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `question` varchar(100) NOT NULL,
  `answer` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `C_App_chatbot_table_USER_id_b3b46006_fk_C_App_user_table_id` (`USER_id`),
  CONSTRAINT `C_App_chatbot_table_USER_id_b3b46006_fk_C_App_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `c_app_user_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `c_app_chatbot_table` */

/*Table structure for table `c_app_complaint_table` */

DROP TABLE IF EXISTS `c_app_complaint_table`;

CREATE TABLE `c_app_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `C_App_complaint_table_USER_id_17d186f3_fk_C_App_user_table_id` (`USER_id`),
  CONSTRAINT `C_App_complaint_table_USER_id_17d186f3_fk_C_App_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `c_app_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `c_app_complaint_table` */

insert  into `c_app_complaint_table`(`id`,`complaint`,`reply`,`date`,`USER_id`) values 
(1,'bad quality','thankyou','2023-09-23',1),
(2,'poor service','we will sort it out','2024-01-04',2);

/*Table structure for table `c_app_dataset_table` */

DROP TABLE IF EXISTS `c_app_dataset_table`;

CREATE TABLE `c_app_dataset_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `question` varchar(100) NOT NULL,
  `answer` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `c_app_dataset_table` */

insert  into `c_app_dataset_table`(`id`,`question`,`answer`) values 
(9,'quality?','nice');

/*Table structure for table `c_app_distributor_product_table` */

DROP TABLE IF EXISTS `c_app_distributor_product_table`;

CREATE TABLE `c_app_distributor_product_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `DISTRIBUTOR_request_id` bigint NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `C_App_distributor_pr_DISTRIBUTOR_request__2467c757_fk_C_App_req` (`DISTRIBUTOR_request_id`),
  KEY `C_App_distributor_pr_PRODUCT_id_da42bc3d_fk_C_App_pro` (`PRODUCT_id`),
  CONSTRAINT `C_App_distributor_pr_DISTRIBUTOR_request__2467c757_fk_C_App_req` FOREIGN KEY (`DISTRIBUTOR_request_id`) REFERENCES `c_app_request_from_distributor` (`id`),
  CONSTRAINT `C_App_distributor_pr_PRODUCT_id_da42bc3d_fk_C_App_pro` FOREIGN KEY (`PRODUCT_id`) REFERENCES `c_app_product_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `c_app_distributor_product_table` */

insert  into `c_app_distributor_product_table`(`id`,`status`,`date`,`DISTRIBUTOR_request_id`,`PRODUCT_id`) values 
(4,'availabale','2024-02-05',3,10),
(5,'available','2024-03-12',4,6),
(6,'available','2024-03-24',7,9);

/*Table structure for table `c_app_distributor_table` */

DROP TABLE IF EXISTS `c_app_distributor_table`;

CREATE TABLE `c_app_distributor_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `id_proof` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `C_App_distributor_ta_LOGIN_id_02f18268_fk_C_App_log` (`LOGIN_id`),
  CONSTRAINT `C_App_distributor_ta_LOGIN_id_02f18268_fk_C_App_log` FOREIGN KEY (`LOGIN_id`) REFERENCES `c_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `c_app_distributor_table` */

insert  into `c_app_distributor_table`(`id`,`name`,`phone`,`email`,`address`,`id_proof`,`LOGIN_id`) values 
(1,'Nikhil',8590545755,'abc@gmail.com','Nileshwar','Aadhar',2),
(2,'partheev',1234567890,'def@gmail.com','alanthatta','aadhar',2);

/*Table structure for table `c_app_feedback_table` */

DROP TABLE IF EXISTS `c_app_feedback_table`;

CREATE TABLE `c_app_feedback_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(100) NOT NULL,
  `rating` double NOT NULL,
  `date` date NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `C_App_feedback_table_PRODUCT_id_43230bf8_fk_C_App_pro` (`PRODUCT_id`),
  KEY `C_App_feedback_table_USER_id_889a5181_fk_C_App_user_table_id` (`USER_id`),
  CONSTRAINT `C_App_feedback_table_PRODUCT_id_43230bf8_fk_C_App_pro` FOREIGN KEY (`PRODUCT_id`) REFERENCES `c_app_product_table` (`id`),
  CONSTRAINT `C_App_feedback_table_USER_id_889a5181_fk_C_App_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `c_app_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `c_app_feedback_table` */

insert  into `c_app_feedback_table`(`id`,`feedback`,`rating`,`date`,`PRODUCT_id`,`USER_id`) values 
(2,'Good',4,'2023-09-11',6,1);

/*Table structure for table `c_app_login_table` */

DROP TABLE IF EXISTS `c_app_login_table`;

CREATE TABLE `c_app_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(10) NOT NULL,
  `password` varchar(10) NOT NULL,
  `type` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `c_app_login_table` */

insert  into `c_app_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','123','admin'),
(2,'distr','123','distributor'),
(3,'shop','123','shop'),
(4,'shop1','123','shop'),
(5,'shop2','123','Rejected'),
(6,'shop2','123','Rejected'),
(7,'wecare','123','Rejected'),
(8,'gmart','123','shop'),
(9,'','','pending'),
(10,'','','pending'),
(11,'shop3','123','shop');

/*Table structure for table `c_app_order_details` */

DROP TABLE IF EXISTS `c_app_order_details`;

CREATE TABLE `c_app_order_details` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `ORDER_id` bigint NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `C_App_order_details_ORDER_id_fb78796f_fk_C_App_order_table_id` (`ORDER_id`),
  KEY `C_App_order_details_PRODUCT_id_ec79759c_fk_C_App_pro` (`PRODUCT_id`),
  CONSTRAINT `C_App_order_details_ORDER_id_fb78796f_fk_C_App_order_table_id` FOREIGN KEY (`ORDER_id`) REFERENCES `c_app_order_table` (`id`),
  CONSTRAINT `C_App_order_details_PRODUCT_id_ec79759c_fk_C_App_pro` FOREIGN KEY (`PRODUCT_id`) REFERENCES `c_app_product_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `c_app_order_details` */

/*Table structure for table `c_app_order_table` */

DROP TABLE IF EXISTS `c_app_order_table`;

CREATE TABLE `c_app_order_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` double NOT NULL,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `USER_id` bigint NOT NULL,
  `SHOP_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `C_App_order_table_SHOP_id_e7940fbb_fk_C_App_shop_table_id` (`SHOP_id`),
  KEY `C_App_order_table_USER_id_517e35e0` (`USER_id`),
  CONSTRAINT `C_App_order_table_SHOP_id_e7940fbb_fk_C_App_shop_table_id` FOREIGN KEY (`SHOP_id`) REFERENCES `c_app_shop_table` (`id`),
  CONSTRAINT `C_App_order_table_USER_id_517e35e0_fk_C_App_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `c_app_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `c_app_order_table` */

insert  into `c_app_order_table`(`id`,`amount`,`status`,`date`,`USER_id`,`SHOP_id`) values 
(1,500,'delivered','2024-02-12',1,1);

/*Table structure for table `c_app_product_table` */

DROP TABLE IF EXISTS `c_app_product_table`;

CREATE TABLE `c_app_product_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `product_name` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `price` double NOT NULL,
  `category` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `c_app_product_table` */

insert  into `c_app_product_table`(`id`,`product_name`,`image`,`price`,`category`) values 
(6,'Refrigerator','refri.png',20000,'Electronics'),
(8,'Watch','watch1.jpeg',500,'Watches'),
(9,'AC','AC.jpeg',5000,'Electronics'),
(10,'Samsung','samsung.jpeg',45000,'Mobiles'),
(11,'sony tv','sony.jpg',25000,'Electronics'),
(13,'Shoe','nike.jpeg',2500,'Footware');

/*Table structure for table `c_app_request_from_distributor` */

DROP TABLE IF EXISTS `c_app_request_from_distributor`;

CREATE TABLE `c_app_request_from_distributor` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `DISTRIBUTOR_id` bigint NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `C_App_request_from_d_DISTRIBUTOR_id_f03525bc_fk_C_App_dis` (`DISTRIBUTOR_id`),
  KEY `C_App_request_from_d_PRODUCT_id_55af8296_fk_C_App_pro` (`PRODUCT_id`),
  CONSTRAINT `C_App_request_from_d_DISTRIBUTOR_id_f03525bc_fk_C_App_dis` FOREIGN KEY (`DISTRIBUTOR_id`) REFERENCES `c_app_distributor_table` (`id`),
  CONSTRAINT `C_App_request_from_d_PRODUCT_id_55af8296_fk_C_App_pro` FOREIGN KEY (`PRODUCT_id`) REFERENCES `c_app_product_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `c_app_request_from_distributor` */

insert  into `c_app_request_from_distributor`(`id`,`quantity`,`status`,`date`,`DISTRIBUTOR_id`,`PRODUCT_id`) values 
(3,3,'pending','2024-02-05',1,9),
(4,3,'Accept','2024-03-24',2,6),
(7,1,'Accept','2024-03-24',2,9);

/*Table structure for table `c_app_request_from_shop` */

DROP TABLE IF EXISTS `c_app_request_from_shop`;

CREATE TABLE `c_app_request_from_shop` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  `SHOP_id` bigint NOT NULL,
  `DISTRIBUTOR_request_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `C_App_request_from_s_PRODUCT_id_7e64fbd6_fk_C_App_pro` (`PRODUCT_id`),
  KEY `C_App_request_from_shop_SHOP_id_9d1672e4_fk_C_App_shop_table_id` (`SHOP_id`),
  KEY `C_App_request_from_s_DISTRIBUTOR_request__840c7e60_fk_C_App_dis` (`DISTRIBUTOR_request_id`),
  CONSTRAINT `C_App_request_from_s_DISTRIBUTOR_request__840c7e60_fk_C_App_dis` FOREIGN KEY (`DISTRIBUTOR_request_id`) REFERENCES `c_app_distributor_table` (`id`),
  CONSTRAINT `C_App_request_from_s_PRODUCT_id_7e64fbd6_fk_C_App_pro` FOREIGN KEY (`PRODUCT_id`) REFERENCES `c_app_product_table` (`id`),
  CONSTRAINT `C_App_request_from_shop_SHOP_id_9d1672e4_fk_C_App_shop_table_id` FOREIGN KEY (`SHOP_id`) REFERENCES `c_app_shop_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `c_app_request_from_shop` */

insert  into `c_app_request_from_shop`(`id`,`quantity`,`status`,`date`,`PRODUCT_id`,`SHOP_id`,`DISTRIBUTOR_request_id`) values 
(1,3,'accepted','2024-03-23',9,2,1),
(2,5,'accepted','2024-03-21',6,2,1),
(3,2,'pending','2024-03-24',6,1,2),
(4,1,'accepted','2024-03-24',10,1,1),
(5,1,'pending','2024-03-24',9,1,2);

/*Table structure for table `c_app_shop_product_table` */

DROP TABLE IF EXISTS `c_app_shop_product_table`;

CREATE TABLE `c_app_shop_product_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  `SHOP_request_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `C_App_shop_product_t_PRODUCT_id_be579f34_fk_C_App_dis` (`PRODUCT_id`),
  KEY `C_App_shop_product_t_SHOP_request_id_de672e80_fk_C_App_req` (`SHOP_request_id`),
  CONSTRAINT `C_App_shop_product_t_PRODUCT_id_be579f34_fk_C_App_dis` FOREIGN KEY (`PRODUCT_id`) REFERENCES `c_app_distributor_product_table` (`id`),
  CONSTRAINT `C_App_shop_product_t_SHOP_request_id_de672e80_fk_C_App_req` FOREIGN KEY (`SHOP_request_id`) REFERENCES `c_app_request_from_shop` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `c_app_shop_product_table` */

insert  into `c_app_shop_product_table`(`id`,`status`,`date`,`PRODUCT_id`,`SHOP_request_id`) values 
(1,'pending','2024-03-23',4,1),
(2,'pending','2024-03-11',5,2);

/*Table structure for table `c_app_shop_table` */

DROP TABLE IF EXISTS `c_app_shop_table`;

CREATE TABLE `c_app_shop_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `shop_name` varchar(20) NOT NULL,
  `address` varchar(100) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `owner_details` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `C_App_shop_table_LOGIN_id_78397f02_fk_C_App_login_table_id` (`LOGIN_id`),
  CONSTRAINT `C_App_shop_table_LOGIN_id_78397f02_fk_C_App_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `c_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `c_app_shop_table` */

insert  into `c_app_shop_table`(`id`,`shop_name`,`address`,`phone`,`email`,`owner_details`,`LOGIN_id`) values 
(1,'MyG','kanhangad',1234567890,'myg@gmail.com','nikhil',3),
(2,'Eplanet','kanhangad',6379256432,'eplanet@gmail.com','niranjan',4),
(7,'Zudio','cheemeni',1234567890,'zudio@gmail.com','Nikhil',11);

/*Table structure for table `c_app_stock_table` */

DROP TABLE IF EXISTS `c_app_stock_table`;

CREATE TABLE `c_app_stock_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `stock` int NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `C_App_stock_table_PRODUCT_id_4ac2d2a9_fk_C_App_product_table_id` (`PRODUCT_id`),
  CONSTRAINT `C_App_stock_table_PRODUCT_id_4ac2d2a9_fk_C_App_product_table_id` FOREIGN KEY (`PRODUCT_id`) REFERENCES `c_app_product_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `c_app_stock_table` */

insert  into `c_app_stock_table`(`id`,`stock`,`PRODUCT_id`) values 
(6,12,6),
(8,10,8),
(9,6,9),
(10,10,10),
(11,3,11);

/*Table structure for table `c_app_user_table` */

DROP TABLE IF EXISTS `c_app_user_table`;

CREATE TABLE `c_app_user_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `C_App_user_table_LOGIN_id_03510f2f_fk_C_App_login_table_id` (`LOGIN_id`),
  CONSTRAINT `C_App_user_table_LOGIN_id_03510f2f_fk_C_App_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `c_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `c_app_user_table` */

insert  into `c_app_user_table`(`id`,`fname`,`lname`,`gender`,`address`,`phone`,`email`,`LOGIN_id`) values 
(1,'job','kurian','male','zxcvbn',12345678,'qwertyuio',2),
(2,'sasi','kuttan','male','hdgtsy',12345678,'dfebtrg',3);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(25,'C_App','bil_details'),
(24,'C_App','bill_table'),
(20,'C_App','chatbot_table'),
(19,'C_App','complaint_table'),
(7,'C_App','dataset_table'),
(21,'C_App','distributor_product_table'),
(8,'C_App','distributor_table'),
(18,'C_App','feedback_table'),
(9,'C_App','login_table'),
(17,'C_App','order_details'),
(16,'C_App','order_table'),
(10,'C_App','product_table'),
(15,'C_App','request_from_distributor'),
(14,'C_App','request_from_shop'),
(23,'C_App','shop_bill_table'),
(22,'C_App','shop_product_table'),
(13,'C_App','shop_table'),
(12,'C_App','stock_table'),
(11,'C_App','user_table'),
(5,'contenttypes','contenttype'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'C_App','0001_initial','2024-02-01 08:26:17.605576'),
(2,'contenttypes','0001_initial','2024-02-01 08:26:17.716418'),
(3,'auth','0001_initial','2024-02-01 08:26:18.723212'),
(4,'admin','0001_initial','2024-02-01 08:26:18.953489'),
(5,'admin','0002_logentry_remove_auto_add','2024-02-01 08:26:18.967671'),
(6,'admin','0003_logentry_add_action_flag_choices','2024-02-01 08:26:18.983849'),
(7,'contenttypes','0002_remove_content_type_name','2024-02-01 08:26:19.097625'),
(8,'auth','0002_alter_permission_name_max_length','2024-02-01 08:26:19.209398'),
(9,'auth','0003_alter_user_email_max_length','2024-02-01 08:26:19.249512'),
(10,'auth','0004_alter_user_username_opts','2024-02-01 08:26:19.266558'),
(11,'auth','0005_alter_user_last_login_null','2024-02-01 08:26:19.381775'),
(12,'auth','0006_require_contenttypes_0002','2024-02-01 08:26:19.388919'),
(13,'auth','0007_alter_validators_add_error_messages','2024-02-01 08:26:19.403342'),
(14,'auth','0008_alter_user_username_max_length','2024-02-01 08:26:19.539504'),
(15,'auth','0009_alter_user_last_name_max_length','2024-02-01 08:26:19.658754'),
(16,'auth','0010_alter_group_name_max_length','2024-02-01 08:26:19.690971'),
(17,'auth','0011_update_proxy_permissions','2024-02-01 08:26:19.715239'),
(18,'auth','0012_alter_user_first_name_max_length','2024-02-01 08:26:19.859815'),
(19,'sessions','0001_initial','2024-02-01 08:26:19.928885'),
(20,'C_App','0002_auto_20240204_1011','2024-02-04 04:41:56.476416'),
(21,'C_App','0003_alter_login_table_type','2024-02-04 05:00:54.618445'),
(22,'C_App','0004_remove_shop_bill_table_user_alter_order_table_user_and_more','2024-02-20 05:54:10.611242'),
(23,'C_App','0005_bill_table_bil_details_delete_shop_bill_table','2024-03-24 05:54:58.251737'),
(24,'C_App','0006_remove_bill_table_user_bill_table_phone_and_more','2024-03-28 05:45:53.855267');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('756aks5xspkg3bg8k23909gvkcz3vmej','e30:1rdRde:wwiokx2_xtAys9gSzwOpUlNb7VWfw0PSpMjPJrlkwZ8','2024-03-08 09:14:38.129286'),
('8szb2hs17d6asgjokj5fx4c6st2ndyrl','eyJsaWQiOjMsImdpZCI6MSwib28iOjZ9:1rpj1B:KHoMQtxaIgvSzBjL3_pN3BhHnpnaghu6l-NXuV92Xy8','2024-04-11 06:13:41.848567'),
('a2fu5lfzcmetxketazxhkhtsevages9m','e30:1rodla:DD4Xe1ZDQilJzkX7l72FDVSfpjRUNXgSnTIopFG30cI','2024-04-08 06:25:06.304063');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
