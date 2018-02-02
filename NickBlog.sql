/*
 Navicat MySQL Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50720
 Source Host           : localhost:3306
 Source Schema         : NickBlog

 Target Server Type    : MySQL
 Target Server Version : 50720
 File Encoding         : 65001

 Date: 02/02/2018 17:30:23
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for account_account
-- ----------------------------
DROP TABLE IF EXISTS `account_account`;
CREATE TABLE `account_account`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `nickname` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for account_account_groups
-- ----------------------------
DROP TABLE IF EXISTS `account_account_groups`;
CREATE TABLE `account_account_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `account_id`(`account_id`, `group_id`) USING BTREE,
  INDEX `account_account_groups_group_id_a1e3a6692296bef_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `account_accoun_account_id_5607020ef3a9651b_fk_account_account_id` FOREIGN KEY (`account_id`) REFERENCES `account_account` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `account_account_groups_group_id_a1e3a6692296bef_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for account_account_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `account_account_user_permissions`;
CREATE TABLE `account_account_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `account_id`(`account_id`, `permission_id`) USING BTREE,
  INDEX `account_acc_permission_id_6fc236dbf74610b3_fk_auth_permission_id`(`permission_id`) USING BTREE,
  CONSTRAINT `account_acc_permission_id_6fc236dbf74610b3_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `account_accoun_account_id_2f02bedb6020e4a1_fk_account_account_id` FOREIGN KEY (`account_id`) REFERENCES `account_account` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for article_article
-- ----------------------------
DROP TABLE IF EXISTS `article_article`;
CREATE TABLE `article_article`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `modified` datetime(6) NOT NULL,
  `last_seen` datetime(6) NOT NULL,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `author` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `view_count` int(11) NOT NULL,
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `remark` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `short_note` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `isDelete` tinyint(1) NOT NULL,
  `article_type_id` int(11) NOT NULL,
  `cover_img` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `title`(`title`) USING BTREE,
  INDEX `article_article_da909a66`(`article_type_id`) USING BTREE,
  CONSTRAINT `artic_article_type_id_78605602ea48e6ab_fk_article_articletype_id` FOREIGN KEY (`article_type_id`) REFERENCES `article_articletype` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for article_article_article_tag
-- ----------------------------
DROP TABLE IF EXISTS `article_article_article_tag`;
CREATE TABLE `article_article_article_tag`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL,
  `tagtype_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `article_id`(`article_id`, `tagtype_id`) USING BTREE,
  INDEX `article_article_tagtype_id_e5f3e954e232857_fk_article_tagtype_id`(`tagtype_id`) USING BTREE,
  CONSTRAINT `article_articl_article_id_670edf09502ca37e_fk_article_article_id` FOREIGN KEY (`article_id`) REFERENCES `article_article` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `article_article_tagtype_id_e5f3e954e232857_fk_article_tagtype_id` FOREIGN KEY (`tagtype_id`) REFERENCES `article_tagtype` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for article_articletype
-- ----------------------------
DROP TABLE IF EXISTS `article_articletype`;
CREATE TABLE `article_articletype`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `modified` datetime(6) NOT NULL,
  `typename` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `isDelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for article_comment
-- ----------------------------
DROP TABLE IF EXISTS `article_comment`;
CREATE TABLE `article_comment`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `modified` datetime(6) NOT NULL,
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `isDelete` tinyint(1) NOT NULL,
  `article_id` int(11) NOT NULL,
  `userOfComment_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `article_commen_article_id_141a5ee31a81f9cf_fk_article_article_id`(`article_id`) USING BTREE,
  INDEX `article_comment_f0565b65`(`userOfComment_id`) USING BTREE,
  CONSTRAINT `article__userOfComment_id_672a8e0e77d7ea3c_fk_account_account_id` FOREIGN KEY (`userOfComment_id`) REFERENCES `account_account` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `article_commen_article_id_141a5ee31a81f9cf_fk_article_article_id` FOREIGN KEY (`article_id`) REFERENCES `article_article` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for article_tagtype
-- ----------------------------
DROP TABLE IF EXISTS `article_tagtype`;
CREATE TABLE `article_tagtype`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `modified` datetime(6) NOT NULL,
  `tag_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `isDelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `group_id`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group__permission_id_7887e0db92d0b662_fk_auth_permission_id`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group__permission_id_7887e0db92d0b662_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permission_group_id_556030ef62eed271_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `content_type_id`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth__content_type_id_1c7816f57be81f63_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 85 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_id`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_3fb769622648581b_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_3fb769622648581b_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_3a8d9f2166c57c0d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_id`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_u_permission_id_507e75daed6477b8_fk_auth_permission_id`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_u_permission_id_507e75daed6477b8_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissi_user_id_5c3add5700833a2b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `djang_content_type_id_6594763d07d79eac_fk_django_content_type_id`(`content_type_id`) USING BTREE,
  INDEX `django_user_id_786fghf`(`user_id`) USING BTREE,
  CONSTRAINT `djang_content_type_id_6594763d07d79eac_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_user_id_786fghf` FOREIGN KEY (`user_id`) REFERENCES `account_account` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_5c05e38fdebe666_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 29 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 38 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_de54fa62`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for hitcount_blacklist_ip
-- ----------------------------
DROP TABLE IF EXISTS `hitcount_blacklist_ip`;
CREATE TABLE `hitcount_blacklist_ip`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `ip`(`ip`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for hitcount_blacklist_user_agent
-- ----------------------------
DROP TABLE IF EXISTS `hitcount_blacklist_user_agent`;
CREATE TABLE `hitcount_blacklist_user_agent`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_agent` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_agent`(`user_agent`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for hitcount_hit
-- ----------------------------
DROP TABLE IF EXISTS `hitcount_hit`;
CREATE TABLE `hitcount_hit`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `ip` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `session` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `user_agent` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `hitcount_id` int(11) NOT NULL,
  `user_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `hitcount_hit_e2fa5388`(`created`) USING BTREE,
  INDEX `hitcount_hit_527d620b`(`hitcount_id`) USING BTREE,
  INDEX `hitcount_hit_e8701ad4`(`user_id`) USING BTREE,
  CONSTRAINT `hitcount_h_hitcount_id_23f26a9fad96a961_fk_hitcount_hit_count_id` FOREIGN KEY (`hitcount_id`) REFERENCES `hitcount_hit_count` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `hitcount_hit_user_id_157f26bf0581710a_fk_account_account_id` FOREIGN KEY (`user_id`) REFERENCES `account_account` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for hitcount_hit_count
-- ----------------------------
DROP TABLE IF EXISTS `hitcount_hit_count`;
CREATE TABLE `hitcount_hit_count`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hits` int(10) UNSIGNED NOT NULL,
  `modified` datetime(6) NOT NULL,
  `object_pk` int(10) UNSIGNED NOT NULL,
  `content_type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `hitcount_hit_count_content_type_id_6930412bd5bdd307_uniq`(`content_type_id`, `object_pk`) USING BTREE,
  CONSTRAINT `hitco_content_type_id_232e73f967722894_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for qa_answer
-- ----------------------------
DROP TABLE IF EXISTS `qa_answer`;
CREATE TABLE `qa_answer`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `answer_text` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `pub_date` datetime(6) NOT NULL,
  `question_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `answer` tinyint(1) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `negative_votes` int(11) NOT NULL,
  `positive_votes` int(11) NOT NULL,
  `total_points` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `qa_answer_7aa0f6ee`(`question_id`) USING BTREE,
  INDEX `qa_answer_e8701ad4`(`user_id`) USING BTREE,
  CONSTRAINT `qa_answer_question_id_415ed235367894a2_fk_qa_question_id` FOREIGN KEY (`question_id`) REFERENCES `qa_question` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `qa_answer_user_id_6eff82f1b5ddccf4_fk_account_account_id` FOREIGN KEY (`user_id`) REFERENCES `account_account` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for qa_answercomment
-- ----------------------------
DROP TABLE IF EXISTS `qa_answercomment`;
CREATE TABLE `qa_answercomment`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pub_date` datetime(6) NOT NULL,
  `comment_text` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `answer_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `qa_answercomment_answer_id_4b58fb7756f0fc7a_fk_qa_answer_id`(`answer_id`) USING BTREE,
  INDEX `qa_answercomment_e8701ad4`(`user_id`) USING BTREE,
  CONSTRAINT `qa_answercomment_answer_id_4b58fb7756f0fc7a_fk_qa_answer_id` FOREIGN KEY (`answer_id`) REFERENCES `qa_answer` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `qa_answercomment_user_id_a79e77b829dbc5b_fk_account_account_id` FOREIGN KEY (`user_id`) REFERENCES `account_account` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for qa_answervote
-- ----------------------------
DROP TABLE IF EXISTS `qa_answervote`;
CREATE TABLE `qa_answervote`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` tinyint(1) NOT NULL,
  `answer_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `qa_answervote_user_id_54d8a07be88f3134_uniq`(`user_id`, `answer_id`) USING BTREE,
  INDEX `qa_answervote_answer_id_2b1df024df1c719f_fk_qa_answer_id`(`answer_id`) USING BTREE,
  INDEX `qa_answervote_e8701ad4`(`user_id`) USING BTREE,
  CONSTRAINT `qa_answervote_answer_id_2b1df024df1c719f_fk_qa_answer_id` FOREIGN KEY (`answer_id`) REFERENCES `qa_answer` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `qa_answervote_user_id_1474a19ceb2e5d66_fk_account_account_id` FOREIGN KEY (`user_id`) REFERENCES `account_account` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for qa_question
-- ----------------------------
DROP TABLE IF EXISTS `qa_question`;
CREATE TABLE `qa_question`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `description` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `pub_date` datetime(6) NOT NULL,
  `reward` int(11) NOT NULL,
  `closed` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  `negative_votes` int(11) NOT NULL,
  `positive_votes` int(11) NOT NULL,
  `total_points` int(11) NOT NULL,
  `slug` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `qa_question_e8701ad4`(`user_id`) USING BTREE,
  INDEX `qa_question_2dbcba41`(`slug`) USING BTREE,
  CONSTRAINT `qa_question_user_id_516147e5b6022ca2_fk_account_account_id` FOREIGN KEY (`user_id`) REFERENCES `account_account` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for qa_questioncomment
-- ----------------------------
DROP TABLE IF EXISTS `qa_questioncomment`;
CREATE TABLE `qa_questioncomment`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pub_date` datetime(6) NOT NULL,
  `comment_text` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `question_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `qa_questioncommen_question_id_1adeb1b0a5cdd658_fk_qa_question_id`(`question_id`) USING BTREE,
  INDEX `qa_questioncomment_e8701ad4`(`user_id`) USING BTREE,
  CONSTRAINT `qa_questioncommen_question_id_1adeb1b0a5cdd658_fk_qa_question_id` FOREIGN KEY (`question_id`) REFERENCES `qa_question` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `qa_questioncommen_user_id_16ae70b63bbf4542_fk_account_account_id` FOREIGN KEY (`user_id`) REFERENCES `account_account` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for qa_questionvote
-- ----------------------------
DROP TABLE IF EXISTS `qa_questionvote`;
CREATE TABLE `qa_questionvote`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` tinyint(1) NOT NULL,
  `question_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `qa_questionvote_user_id_2c9462b029a1fe26_uniq`(`user_id`, `question_id`) USING BTREE,
  INDEX `qa_questionvote_question_id_7548e4ae0a45f9c5_fk_qa_question_id`(`question_id`) USING BTREE,
  INDEX `qa_questionvote_e8701ad4`(`user_id`) USING BTREE,
  CONSTRAINT `qa_questionvote_question_id_7548e4ae0a45f9c5_fk_qa_question_id` FOREIGN KEY (`question_id`) REFERENCES `qa_question` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `qa_questionvote_user_id_14ed8240d371c69b_fk_account_account_id` FOREIGN KEY (`user_id`) REFERENCES `account_account` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for qa_userqaprofile
-- ----------------------------
DROP TABLE IF EXISTS `qa_userqaprofile`;
CREATE TABLE `qa_userqaprofile`  (
  `user_id` int(11) NOT NULL,
  `points` int(11) NOT NULL,
  `website` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`user_id`) USING BTREE,
  CONSTRAINT `qa_userqaprofile_user_id_749d80958fbd13dc_fk_account_account_id` FOREIGN KEY (`user_id`) REFERENCES `account_account` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for silk_profile
-- ----------------------------
DROP TABLE IF EXISTS `silk_profile`;
CREATE TABLE `silk_profile`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NULL DEFAULT NULL,
  `time_taken` double NULL DEFAULT NULL,
  `file_path` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `line_num` int(11) NULL DEFAULT NULL,
  `end_line_num` int(11) NULL DEFAULT NULL,
  `func_name` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `exception_raised` tinyint(1) NOT NULL,
  `dynamic` tinyint(1) NOT NULL,
  `request_id` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `silk_profile_f68d2c36`(`request_id`) USING BTREE,
  CONSTRAINT `silk_profile_request_id_79eaeed18a0621b7_fk_silk_request_id` FOREIGN KEY (`request_id`) REFERENCES `silk_request` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for silk_profile_queries
-- ----------------------------
DROP TABLE IF EXISTS `silk_profile_queries`;
CREATE TABLE `silk_profile_queries`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profile_id` int(11) NOT NULL,
  `sqlquery_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `profile_id`(`profile_id`, `sqlquery_id`) USING BTREE,
  INDEX `silk_profile_qu_sqlquery_id_480574bcbd5a0851_fk_silk_sqlquery_id`(`sqlquery_id`) USING BTREE,
  CONSTRAINT `silk_profile_qu_sqlquery_id_480574bcbd5a0851_fk_silk_sqlquery_id` FOREIGN KEY (`sqlquery_id`) REFERENCES `silk_sqlquery` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `silk_profile_quer_profile_id_652666e24c346258_fk_silk_profile_id` FOREIGN KEY (`profile_id`) REFERENCES `silk_profile` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for silk_request
-- ----------------------------
DROP TABLE IF EXISTS `silk_request`;
CREATE TABLE `silk_request`  (
  `id` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `path` varchar(190) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `query_params` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `raw_body` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `body` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `method` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `view_name` varchar(190) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `end_time` datetime(6) NULL DEFAULT NULL,
  `time_taken` double NULL DEFAULT NULL,
  `encoded_headers` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `meta_time` double NULL DEFAULT NULL,
  `meta_num_queries` int(11) NULL DEFAULT NULL,
  `meta_time_spent_queries` double NULL DEFAULT NULL,
  `pyprofile` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `num_sql_queries` int(11) NOT NULL,
  `prof_file` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `silk_request_d6fe1d0b`(`path`) USING BTREE,
  INDEX `silk_request_c4d98dbd`(`start_time`) USING BTREE,
  INDEX `silk_request_fdbe71b4`(`view_name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for silk_response
-- ----------------------------
DROP TABLE IF EXISTS `silk_response`;
CREATE TABLE `silk_response`  (
  `id` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `status_code` int(11) NOT NULL,
  `raw_body` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `body` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `encoded_headers` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `request_id` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `request_id`(`request_id`) USING BTREE,
  CONSTRAINT `silk_response_request_id_67143c82c89efb6_fk_silk_request_id` FOREIGN KEY (`request_id`) REFERENCES `silk_request` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for silk_sqlquery
-- ----------------------------
DROP TABLE IF EXISTS `silk_sqlquery`;
CREATE TABLE `silk_sqlquery`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `query` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `start_time` datetime(6) NULL DEFAULT NULL,
  `end_time` datetime(6) NULL DEFAULT NULL,
  `time_taken` double NULL DEFAULT NULL,
  `traceback` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `request_id` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `silk_sqlquery_request_id_1eb98eafff448948_fk_silk_request_id`(`request_id`) USING BTREE,
  CONSTRAINT `silk_sqlquery_request_id_1eb98eafff448948_fk_silk_request_id` FOREIGN KEY (`request_id`) REFERENCES `silk_request` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 14231 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for taggit_tag
-- ----------------------------
DROP TABLE IF EXISTS `taggit_tag`;
CREATE TABLE `taggit_tag`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `slug` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  UNIQUE INDEX `slug`(`slug`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for taggit_taggeditem
-- ----------------------------
DROP TABLE IF EXISTS `taggit_taggeditem`;
CREATE TABLE `taggit_taggeditem`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `object_id` int(11) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `taggit_taggeditem_tag_id_5b143999fe183605_fk_taggit_tag_id`(`tag_id`) USING BTREE,
  INDEX `taggit_taggeditem_af31437c`(`object_id`) USING BTREE,
  INDEX `taggit_taggeditem_content_type_id_54efedefdf1523b1_idx`(`content_type_id`, `object_id`) USING BTREE,
  CONSTRAINT `taggit_content_type_id_ab6401b84bc7bb9_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `taggit_taggeditem_tag_id_5b143999fe183605_fk_taggit_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `taggit_tag` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
