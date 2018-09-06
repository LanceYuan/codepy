/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50723
Source Host           : localhost:3306
Source Database       : codepy

Target Server Type    : MYSQL
Target Server Version : 50723
File Encoding         : 65001

Date: 2018-09-06 15:55:42
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app01_author
-- ----------------------------
INSERT INTO `app01_author` VALUES ('3', 'LanceYuan', '2018-09-06 15:48:58.811943', '2018-09-06 15:49:00.121228');
INSERT INTO `app01_author` VALUES ('7', 'Lily', '2018-09-06 15:48:58.811943', '2018-09-06 15:49:00.121228');
INSERT INTO `app01_author` VALUES ('8', 'Caption', '2018-09-06 15:48:58.811943', '2018-09-06 15:49:00.121228');

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
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app01_author_book
-- ----------------------------
INSERT INTO `app01_author_book` VALUES ('2', '3', '3');
INSERT INTO `app01_author_book` VALUES ('3', '3', '6');
INSERT INTO `app01_author_book` VALUES ('22', '7', '3');
INSERT INTO `app01_author_book` VALUES ('23', '7', '7');
INSERT INTO `app01_author_book` VALUES ('25', '8', '3');
INSERT INTO `app01_author_book` VALUES ('26', '8', '6');
INSERT INTO `app01_author_book` VALUES ('24', '8', '8');

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
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `app01_book_publisher_id_e407867a_fk_app01_publisher_id` (`publisher_id`),
  CONSTRAINT `app01_book_publisher_id_e407867a_fk_app01_publisher_id` FOREIGN KEY (`publisher_id`) REFERENCES `app01_publisher` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app01_book
-- ----------------------------
INSERT INTO `app01_book` VALUES ('3', 'Python 全栈', '6', '2018-09-06 15:49:00.963883', '2018-09-06 15:49:01.846978');
INSERT INTO `app01_book` VALUES ('6', 'Go lang高并发', '3', '2018-09-06 15:49:00.963883', '2018-09-06 15:49:01.846978');
INSERT INTO `app01_book` VALUES ('7', '英语ABC', '1', '2018-09-06 15:49:00.963883', '2018-09-06 15:49:01.846978');
INSERT INTO `app01_book` VALUES ('8', 'java script 万能', '3', '2018-09-06 15:49:00.963883', '2018-09-06 15:49:01.846978');
INSERT INTO `app01_book` VALUES ('9', '战神', '1', '2018-09-06 15:49:00.963883', '2018-09-06 15:49:01.846978');
INSERT INTO `app01_book` VALUES ('10', '北漂', '8', '2018-09-06 15:49:00.963883', '2018-09-06 15:49:01.846978');

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
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('9', 'app01', 'author');
INSERT INTO `django_content_type` VALUES ('8', 'app01', 'book');
INSERT INTO `django_content_type` VALUES ('7', 'app01', 'publisher');
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
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

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
