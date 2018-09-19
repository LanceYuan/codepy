/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50723
Source Host           : localhost:3306
Source Database       : codepy

Target Server Type    : MYSQL
Target Server Version : 50723
File Encoding         : 65001

Date: 2018-09-18 16:21:20
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for app01_author
-- ----------------------------
DROP TABLE IF EXISTS `app01_author`;
CREATE TABLE `app01_author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `detail_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `detail_id` (`detail_id`),
  CONSTRAINT `app01_author_detail_id_87f03617_fk_app01_authordetail_id` FOREIGN KEY (`detail_id`) REFERENCES `app01_authordetail` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app01_author
-- ----------------------------
INSERT INTO `app01_author` VALUES ('9', 'Lance', '2018-09-09 11:41:45.874763', '2018-09-09 11:43:43.417487', '1');
INSERT INTO `app01_author` VALUES ('11', 'Lily', '2018-09-09 11:44:01.894543', '2018-09-09 11:44:01.894543', '2');
INSERT INTO `app01_author` VALUES ('12', 'Caption', '2018-09-09 11:45:11.001496', '2018-09-09 11:45:11.001496', '3');

-- ----------------------------
-- Table structure for app01_authordetail
-- ----------------------------
DROP TABLE IF EXISTS `app01_authordetail`;
CREATE TABLE `app01_authordetail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `addr` varchar(128) NOT NULL,
  `language` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app01_authordetail
-- ----------------------------
INSERT INTO `app01_authordetail` VALUES ('1', 'SH', 'Python');
INSERT INTO `app01_authordetail` VALUES ('2', 'SZ', 'Java');
INSERT INTO `app01_authordetail` VALUES ('3', 'ZZ', 'Go');

-- ----------------------------
-- Table structure for app01_author_book
-- ----------------------------
DROP TABLE IF EXISTS `app01_author_book`;
CREATE TABLE `app01_author_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author_id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app01_author_book_author_id_2a845453_uniq` (`author_id`,`book_id`),
  KEY `app01_author_book_book_id_15e32827_fk_app01_book_id` (`book_id`),
  CONSTRAINT `app01_author_book_author_id_0f6c5f17_fk_app01_author_id` FOREIGN KEY (`author_id`) REFERENCES `app01_author` (`id`),
  CONSTRAINT `app01_author_book_book_id_15e32827_fk_app01_book_id` FOREIGN KEY (`book_id`) REFERENCES `app01_book` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app01_author_book
-- ----------------------------
INSERT INTO `app01_author_book` VALUES ('43', '9', '3');
INSERT INTO `app01_author_book` VALUES ('42', '9', '6');
INSERT INTO `app01_author_book` VALUES ('41', '9', '12');
INSERT INTO `app01_author_book` VALUES ('40', '9', '14');
INSERT INTO `app01_author_book` VALUES ('44', '11', '7');
INSERT INTO `app01_author_book` VALUES ('45', '11', '11');
INSERT INTO `app01_author_book` VALUES ('46', '12', '6');

-- ----------------------------
-- Table structure for app01_book
-- ----------------------------
DROP TABLE IF EXISTS `app01_book`;
CREATE TABLE `app01_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `publisher_id` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `price` decimal(5,2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `app01_book_publisher_id_e407867a_fk_app01_publisher_id` (`publisher_id`),
  CONSTRAINT `app01_book_publisher_id_e407867a_fk_app01_publisher_id` FOREIGN KEY (`publisher_id`) REFERENCES `app01_publisher` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app01_book
-- ----------------------------
INSERT INTO `app01_book` VALUES ('3', 'Python全栈S10', '6', '2018-09-06 15:49:00.963883', '2018-09-08 15:55:40.051060', '479.96');
INSERT INTO `app01_book` VALUES ('6', 'Go lang高并发', '3', '2018-09-06 15:49:00.963883', '2018-09-06 15:49:00.963883', '959.96');
INSERT INTO `app01_book` VALUES ('7', '英语ABC', '1', '2018-09-06 15:49:00.963883', '2018-09-06 15:49:00.963883', '470.36');
INSERT INTO `app01_book` VALUES ('8', 'JavaScript万能', '3', '2018-09-06 15:49:00.963883', '2018-09-08 15:55:57.863079', '425.56');
INSERT INTO `app01_book` VALUES ('10', '北漂', '8', '2018-09-06 15:49:00.963883', '2018-09-06 15:49:00.963883', '108.24');
INSERT INTO `app01_book` VALUES ('11', 'Java并发编程', '6', '2018-09-08 16:35:44.109564', '2018-09-08 16:35:44.110564', '4.76');
INSERT INTO `app01_book` VALUES ('12', 'Django 开发', '6', '2018-09-08 18:48:50.943385', '2018-09-08 18:48:50.943385', '666.66');
INSERT INTO `app01_book` VALUES ('14', 'Flask Web开发', '1', '2018-09-08 21:07:52.293483', '2018-09-08 21:07:52.293483', '479.96');
INSERT INTO `app01_book` VALUES ('15', '人类简史', '8', '2018-09-10 16:00:56.957736', '2018-09-10 16:00:56.957736', '99.99');
INSERT INTO `app01_book` VALUES ('16', 'codepy高性能开发', '2', '2018-09-10 16:01:45.800588', '2018-09-10 16:01:45.801584', '99.99');

-- ----------------------------
-- Table structure for app01_publisher
-- ----------------------------
DROP TABLE IF EXISTS `app01_publisher`;
CREATE TABLE `app01_publisher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app01_publisher
-- ----------------------------
INSERT INTO `app01_publisher` VALUES ('1', '新华出版社', '2018-09-06 15:49:02.687071', '2018-09-06 15:49:03.540491');
INSERT INTO `app01_publisher` VALUES ('2', '电子工业出版社', '2018-09-06 15:49:02.687071', '2018-09-06 15:49:03.540491');
INSERT INTO `app01_publisher` VALUES ('3', '上海出版社', '2018-09-06 15:49:02.687071', '2018-09-06 15:49:03.540491');
INSERT INTO `app01_publisher` VALUES ('5', '清华出版社', '2018-09-06 15:49:02.687071', '2018-09-06 15:49:03.540491');
INSERT INTO `app01_publisher` VALUES ('6', '上海老男孩出版社', '2018-09-06 15:49:02.687071', '2018-09-06 15:51:32.325860');
INSERT INTO `app01_publisher` VALUES ('7', '上海新东方出版社', '2018-09-06 15:49:02.687071', '2018-09-06 15:49:03.540491');
INSERT INTO `app01_publisher` VALUES ('8', '北京出版社', '2018-09-06 15:49:02.687071', '2018-09-06 15:49:03.540491');

-- ----------------------------
-- Table structure for app01_userinfo
-- ----------------------------
DROP TABLE IF EXISTS `app01_userinfo`;
CREATE TABLE `app01_userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` varchar(64) NOT NULL,
  `email` varchar(32) DEFAULT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `gender` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app01_userinfo
-- ----------------------------
INSERT INTO `app01_userinfo` VALUES ('4', 'lanceyuan', 'LANCEyuan88', '44480466@qq.com', 'upload/ubuntu.png', '1');

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add user', '3', 'add_user');
INSERT INTO `auth_permission` VALUES ('8', 'Can change user', '3', 'change_user');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete user', '3', 'delete_user');
INSERT INTO `auth_permission` VALUES ('10', 'Can add group', '4', 'add_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can change group', '4', 'change_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete group', '4', 'delete_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add publisher', '7', 'add_publisher');
INSERT INTO `auth_permission` VALUES ('20', 'Can change publisher', '7', 'change_publisher');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete publisher', '7', 'delete_publisher');
INSERT INTO `auth_permission` VALUES ('22', 'Can add book', '8', 'add_book');
INSERT INTO `auth_permission` VALUES ('23', 'Can change book', '8', 'change_book');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete book', '8', 'delete_book');
INSERT INTO `auth_permission` VALUES ('25', 'Can add author', '9', 'add_author');
INSERT INTO `auth_permission` VALUES ('26', 'Can change author', '9', 'change_author');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete author', '9', 'delete_author');
INSERT INTO `auth_permission` VALUES ('28', 'Can add author detail', '10', 'add_authordetail');
INSERT INTO `auth_permission` VALUES ('29', 'Can change author detail', '10', 'change_authordetail');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete author detail', '10', 'delete_authordetail');
INSERT INTO `auth_permission` VALUES ('31', 'Can add userinfo', '11', 'add_userinfo');
INSERT INTO `auth_permission` VALUES ('32', 'Can change userinfo', '11', 'change_userinfo');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete userinfo', '11', 'delete_userinfo');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$36000$I6o2njHlSZJY$QjwXgbBHwoQ9el0T9Rx493+VAo3br0UutaZGmsRznS0=', '2018-09-17 17:21:53.671539', '1', 'lance', '', '', 'lanceyuan.ly@gmail.com', '1', '1', '2018-09-17 08:44:02.556027');
INSERT INTO `auth_user` VALUES ('3', 'pbkdf2_sha256$36000$kwc9OdgvC1qt$J4iXzf6cq9k/Bqns8/JETv5k+ATJCy93etvjm8ysma8=', '2018-09-17 17:21:39.774500', '0', 'lily', '', '', '4448', '0', '1', '2018-09-17 11:21:32.168991');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('9', 'app01', 'author');
INSERT INTO `django_content_type` VALUES ('10', 'app01', 'authordetail');
INSERT INTO `django_content_type` VALUES ('8', 'app01', 'book');
INSERT INTO `django_content_type` VALUES ('7', 'app01', 'publisher');
INSERT INTO `django_content_type` VALUES ('11', 'app01', 'userinfo');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-09-03 10:02:12.725860');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2018-09-03 10:02:21.668829');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2018-09-03 10:02:23.876796');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2018-09-03 10:02:23.952949');
INSERT INTO `django_migrations` VALUES ('5', 'app01', '0001_initial', '2018-09-03 10:02:24.355199');
INSERT INTO `django_migrations` VALUES ('6', 'contenttypes', '0002_remove_content_type_name', '2018-09-03 10:02:25.780128');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0002_alter_permission_name_max_length', '2018-09-03 10:02:26.621284');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0003_alter_user_email_max_length', '2018-09-03 10:02:27.524235');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0004_alter_user_username_opts', '2018-09-03 10:02:27.598504');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0005_alter_user_last_login_null', '2018-09-03 10:02:28.267821');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0006_require_contenttypes_0002', '2018-09-03 10:02:28.312760');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0007_alter_validators_add_error_messages', '2018-09-03 10:02:28.382164');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0008_alter_user_username_max_length', '2018-09-03 10:02:29.202832');
INSERT INTO `django_migrations` VALUES ('14', 'sessions', '0001_initial', '2018-09-03 10:02:29.792459');
INSERT INTO `django_migrations` VALUES ('15', 'app01', '0002_book', '2018-09-03 12:45:41.847260');
INSERT INTO `django_migrations` VALUES ('16', 'app01', '0003_author', '2018-09-04 11:47:58.681639');
INSERT INTO `django_migrations` VALUES ('17', 'app01', '0004_auto_20180906_1548', '2018-09-06 15:49:04.524092');
INSERT INTO `django_migrations` VALUES ('18', 'app01', '0005_book_price', '2018-09-08 21:05:36.485715');
INSERT INTO `django_migrations` VALUES ('19', 'app01', '0006_authordetail', '2018-09-09 11:39:25.594740');
INSERT INTO `django_migrations` VALUES ('20', 'app01', '0007_author_detail', '2018-09-09 11:40:00.390730');
INSERT INTO `django_migrations` VALUES ('21', 'app01', '0008_userinfo', '2018-09-18 08:25:51.171368');
INSERT INTO `django_migrations` VALUES ('22', 'app01', '0009_userinfo_gender', '2018-09-18 08:37:10.631347');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
