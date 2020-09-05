/*
Navicat MySQL Data Transfer

Source Server         : myWebTestSql
Source Server Version : 50527
Source Host           : localhost:3306
Source Database       : pythonsql

Target Server Type    : MYSQL
Target Server Version : 50527
File Encoding         : 65001

Date: 2020-09-06 00:41:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `news_gzbd`
-- ----------------------------
DROP TABLE IF EXISTS `news_gzbd`;
CREATE TABLE `news_gzbd` (
  `news_gzbd_id` int(11) NOT NULL AUTO_INCREMENT,
  `news_gzbd_district` varchar(255) DEFAULT NULL,
  `news_gzbd_time` varchar(255) DEFAULT NULL,
  `news_gzbd_confirmed` int(255) DEFAULT NULL,
  `news_gzbd_outsideinput` int(255) DEFAULT NULL,
  `news_gzbd_cure` int(255) DEFAULT NULL,
  `news_gzbd_death` int(255) DEFAULT NULL,
  `news_gzbd_isolation` int(255) DEFAULT NULL,
  `news_gzbd_observe` int(255) DEFAULT NULL,
  PRIMARY KEY (`news_gzbd_id`)
) ENGINE=InnoDB AUTO_INCREMENT=513 DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of news_gzbd
-- ----------------------------
INSERT INTO `news_gzbd` VALUES ('367', '四川省', '9月4日', '656', '115', '632', '3', '21', '927');
INSERT INTO `news_gzbd` VALUES ('368', '四川省', '9月3日', '655', '114', '630', '3', '22', '926');
INSERT INTO `news_gzbd` VALUES ('369', '四川省', '9月2日', '653', '112', '626', '3', '24', '964');
INSERT INTO `news_gzbd` VALUES ('370', '四川省', '9月1日', '652', '111', '624', '3', '25', '880');
INSERT INTO `news_gzbd` VALUES ('371', '四川省', '8月31日', '652', '111', '622', '3', '27', '822');
INSERT INTO `news_gzbd` VALUES ('372', '四川省', '8月30日', '652', '111', '622', '3', '27', '864');
INSERT INTO `news_gzbd` VALUES ('373', '四川省', '8月29日', '650', '109', '622', '3', '25', '882');
INSERT INTO `news_gzbd` VALUES ('374', '四川省', '8月28日', '648', '107', '620', '3', '25', '827');
INSERT INTO `news_gzbd` VALUES ('375', '四川省', '8月27日', '644', '103', '619', '3', '22', '895');
INSERT INTO `news_gzbd` VALUES ('376', '四川省', '8月26日', '640', '99', '617', '3', '20', '988');
INSERT INTO `news_gzbd` VALUES ('377', '四川省', '8月25日', '635', '94', '615', '3', '17', '932');
INSERT INTO `news_gzbd` VALUES ('378', '四川省', '8月24日', '631', '90', '611', '3', '17', '791');
INSERT INTO `news_gzbd` VALUES ('379', '四川省', '8月23日', '628', '87', '611', '3', '14', '439');
INSERT INTO `news_gzbd` VALUES ('380', '四川省', '8月22日', '628', '87', '611', '3', '14', '554');
INSERT INTO `news_gzbd` VALUES ('381', '四川省', '8月21日', '628', '87', '610', '3', '15', '554');
INSERT INTO `news_gzbd` VALUES ('382', '四川省', '8月20日', '627', '86', '609', '3', '15', '551');
INSERT INTO `news_gzbd` VALUES ('383', '四川省', '8月19日', '626', '85', '609', '3', '14', '455');
INSERT INTO `news_gzbd` VALUES ('384', '四川省', '8月18日', '626', '85', '608', '3', '15', '481');
INSERT INTO `news_gzbd` VALUES ('385', '四川省', '8月17日', '626', '85', null, null, null, null);
INSERT INTO `news_gzbd` VALUES ('386', '四川省', '8月16日', '624', '83', '606', '3', '15', '539');
INSERT INTO `news_gzbd` VALUES ('387', '四川省', '8月15日', '623', '82', '606', '3', '14', '548');
INSERT INTO `news_gzbd` VALUES ('388', '四川省', '8月14日', '619', '78', '605', '3', '11', '545');
INSERT INTO `news_gzbd` VALUES ('389', '四川省', '8月13日', '618', '77', '602', '3', '13', '549');
INSERT INTO `news_gzbd` VALUES ('390', '四川省', '8月12日', '616', '75', '600', '3', '13', '437');
INSERT INTO `news_gzbd` VALUES ('391', '四川省', '8月11日', '615', '74', '599', '3', '13', '437');
INSERT INTO `news_gzbd` VALUES ('392', '四川省', '8月10日', '615', '74', '599', '3', '13', '437');
INSERT INTO `news_gzbd` VALUES ('393', '四川省', '8月9日', '611', '70', '599', '3', '9', '322');
INSERT INTO `news_gzbd` VALUES ('394', '四川省', '8月8日', '611', '70', '599', '3', '9', '365');
INSERT INTO `news_gzbd` VALUES ('395', '四川省', '8月7日', '611', '70', '599', '3', '9', '366');
INSERT INTO `news_gzbd` VALUES ('396', '四川省', '8月6日', '610', '69', '598', '3', '9', '340');
INSERT INTO `news_gzbd` VALUES ('397', '四川省', '8月5日', '610', '69', '598', '3', '9', '340');
INSERT INTO `news_gzbd` VALUES ('398', '四川省', '8月4日', '609', '68', '597', '3', '9', '280');
INSERT INTO `news_gzbd` VALUES ('399', '四川省', '8月3日', '608', '67', '597', '3', '8', '280');
INSERT INTO `news_gzbd` VALUES ('400', '四川省', '8月2日', '608', '67', '597', '3', '8', '413');
INSERT INTO `news_gzbd` VALUES ('401', '四川省', '8月1日', '604', '63', '597', '3', '4', '277');
INSERT INTO `news_gzbd` VALUES ('402', '四川省', '7月31日', '604', '63', '597', '3', '4', '277');
INSERT INTO `news_gzbd` VALUES ('403', '四川省', '7月30日', '604', '63', '596', '3', '5', '278');
INSERT INTO `news_gzbd` VALUES ('404', '四川省', '7月29日', '604', '63', '596', '3', '5', '278');
INSERT INTO `news_gzbd` VALUES ('405', '四川省', '7月28日', '604', '63', '595', '3', '6', '280');
INSERT INTO `news_gzbd` VALUES ('406', '四川省', '7月27日', '604', '63', '594', '3', '7', '279');
INSERT INTO `news_gzbd` VALUES ('407', '四川省', '7月26日', '603', '62', '594', '3', '6', '236');
INSERT INTO `news_gzbd` VALUES ('408', '四川省', '7月25日', '603', '62', '594', '3', '6', '236');
INSERT INTO `news_gzbd` VALUES ('409', '四川省', '7月24日', '603', '62', '594', '3', '6', '236');
INSERT INTO `news_gzbd` VALUES ('410', '四川省', '7月23日', '603', '62', '594', '3', '6', '255');
INSERT INTO `news_gzbd` VALUES ('411', '四川省', '7月22日', '603', '62', '593', '3', '7', '282');
INSERT INTO `news_gzbd` VALUES ('412', '四川省', '7月21日', '603', '62', '593', '3', '7', '275');
INSERT INTO `news_gzbd` VALUES ('413', '四川省', '7月20日', '602', '61', '592', '3', '7', '379');
INSERT INTO `news_gzbd` VALUES ('414', '四川省', '7月19日', '599', '58', '592', '3', '4', '203');
INSERT INTO `news_gzbd` VALUES ('415', '四川省', '7月18日', '599', '58', '592', '3', '4', '203');
INSERT INTO `news_gzbd` VALUES ('416', '四川省', '7月17日', '599', '58', '591', '3', '5', '209');
INSERT INTO `news_gzbd` VALUES ('417', '四川省', '7月16日', '599', '58', '590', '3', '6', '209');
INSERT INTO `news_gzbd` VALUES ('418', '四川省', '7月15日', '599', '58', '589', '3', '7', '209');
INSERT INTO `news_gzbd` VALUES ('419', '四川省', '7月14日', '599', '58', '589', '3', '7', '208');
INSERT INTO `news_gzbd` VALUES ('420', '四川省', '7月13日', '599', '58', '587', '3', '9', '268');
INSERT INTO `news_gzbd` VALUES ('421', '四川省', '7月12日', '599', '58', '587', '3', '9', '269');
INSERT INTO `news_gzbd` VALUES ('422', '四川省', '7月11日', '599', '58', '587', '3', '9', '269');
INSERT INTO `news_gzbd` VALUES ('423', '四川省', '7月10日', '599', '58', '585', '3', '11', '273');
INSERT INTO `news_gzbd` VALUES ('424', '四川省', '7月9日', '599', '58', '582', '3', '14', '263');
INSERT INTO `news_gzbd` VALUES ('425', '四川省', '7月8日', '598', '57', '581', '3', '14', '312');
INSERT INTO `news_gzbd` VALUES ('426', '四川省', '7月7日', '598', '57', '581', '3', '14', '296');
INSERT INTO `news_gzbd` VALUES ('427', '四川省', '7月6日', '596', '55', '581', '3', '12', '226');
INSERT INTO `news_gzbd` VALUES ('428', '四川省', '7月5日', '596', '55', '581', '3', '12', '185');
INSERT INTO `news_gzbd` VALUES ('429', '四川省', '7月4日', '595', '54', '581', '3', '11', '193');
INSERT INTO `news_gzbd` VALUES ('430', '四川省', '7月3日', '595', '54', '581', '3', '11', '209');
INSERT INTO `news_gzbd` VALUES ('431', '四川省', '7月2日', '595', '54', '580', '3', '12', '221');
INSERT INTO `news_gzbd` VALUES ('432', '四川省', '7月1日', '595', '54', '580', '3', '12', '258');
INSERT INTO `news_gzbd` VALUES ('433', '四川省', '6月30日', '595', '54', '578', '3', '14', '317');
INSERT INTO `news_gzbd` VALUES ('434', '四川省', '6月29日', '592', '51', '577', '3', '12', '323');
INSERT INTO `news_gzbd` VALUES ('435', '四川省', '6月28日', '589', '48', '575', '3', '11', '263');
INSERT INTO `news_gzbd` VALUES ('436', '四川省', '6月27日', '589', '48', '575', '3', '11', '348');
INSERT INTO `news_gzbd` VALUES ('437', '四川省', '6月26日', '589', '48', '575', '3', '11', '371');
INSERT INTO `news_gzbd` VALUES ('438', '四川省', '6月25日', '589', '48', '575', '3', '11', '312');
INSERT INTO `news_gzbd` VALUES ('439', '四川省', '6月24日', '589', '48', '573', '3', '13', '311');
INSERT INTO `news_gzbd` VALUES ('440', '四川省', '6月23日', '589', '48', '572', '3', '14', '311');
INSERT INTO `news_gzbd` VALUES ('441', '四川省', '6月22日', '589', '48', '570', '3', '16', '300');
INSERT INTO `news_gzbd` VALUES ('442', '四川省', '6月21日', '589', '48', '570', '3', '16', '271');
INSERT INTO `news_gzbd` VALUES ('443', '四川省', '6月20日', '589', '48', '570', '3', '16', '392');
INSERT INTO `news_gzbd` VALUES ('444', '四川省', '6月19日', '589', '48', '569', '3', '17', '372');
INSERT INTO `news_gzbd` VALUES ('445', '四川省', '6月18日', '589', '48', '567', '3', '19', '360');
INSERT INTO `news_gzbd` VALUES ('446', '四川省', '6月17日', '589', '48', '565', '3', '21', '353');
INSERT INTO `news_gzbd` VALUES ('447', '四川省', '6月16日', '588', '47', '564', '3', '21', '331');
INSERT INTO `news_gzbd` VALUES ('448', '四川省', '6月15日', '587', '47', '563', '3', '21', '272');
INSERT INTO `news_gzbd` VALUES ('449', '四川省', '6月14日', '583', '43', '563', '3', '17', '184');
INSERT INTO `news_gzbd` VALUES ('450', '四川省', '6月13日', '583', '43', '562', '3', '18', '382');
INSERT INTO `news_gzbd` VALUES ('451', '四川省', '6月12日', '582', '42', '561', '3', '18', '360');
INSERT INTO `news_gzbd` VALUES ('452', '四川省', '6月11日', '582', '42', '560', '3', '19', '358');
INSERT INTO `news_gzbd` VALUES ('453', '四川省', '6月10日', '582', '42', '558', '3', '21', '358');
INSERT INTO `news_gzbd` VALUES ('454', '四川省', '6月9日', '582', '42', '558', '3', '21', '358');
INSERT INTO `news_gzbd` VALUES ('455', '四川省', '6月8日', '581', '41', '558', '3', '20', '359');
INSERT INTO `news_gzbd` VALUES ('456', '四川省', '6月7日', '578', '38', '558', '3', '17', '262');
INSERT INTO `news_gzbd` VALUES ('457', '四川省', '6月6日', '578', '38', '558', '3', '17', '306');
INSERT INTO `news_gzbd` VALUES ('458', '四川省', '6月5日', '578', '38', '558', '3', '17', '307');
INSERT INTO `news_gzbd` VALUES ('459', '四川省', '6月4日', '577', '37', '558', '3', '16', '296');
INSERT INTO `news_gzbd` VALUES ('460', '四川省', '6月3日', '577', '37', '558', '3', '16', '322');
INSERT INTO `news_gzbd` VALUES ('461', '四川省', '6月2日', '577', '37', '558', '3', '16', '322');
INSERT INTO `news_gzbd` VALUES ('462', '四川省', '6月1日', null, null, null, null, null, null);
INSERT INTO `news_gzbd` VALUES ('463', '四川省', '5月31日', '564', '24', '558', '3', '3', '117');
INSERT INTO `news_gzbd` VALUES ('464', '四川省', '5月30日', '564', '24', '558', '3', '3', '117');
INSERT INTO `news_gzbd` VALUES ('465', '四川省', '5月29日', '564', '24', '558', '3', '3', '116');
INSERT INTO `news_gzbd` VALUES ('466', '四川省', '5月28日', '564', '24', '558', '3', '3', '116');
INSERT INTO `news_gzbd` VALUES ('467', '四川省', '5月27日', '564', '24', '558', '3', '3', '114');
INSERT INTO `news_gzbd` VALUES ('468', '四川省', '5月26日', '564', '24', '558', '3', '3', '106');
INSERT INTO `news_gzbd` VALUES ('469', '四川省', '5月25日', '564', '24', '558', '3', '3', '94');
INSERT INTO `news_gzbd` VALUES ('470', '四川省', '5月24日', '563', '23', '558', '3', '2', '26');
INSERT INTO `news_gzbd` VALUES ('471', '四川省', '5月23日', '563', '23', '558', '3', '2', '26');
INSERT INTO `news_gzbd` VALUES ('472', '四川省', '5月22日', '563', '23', '2', '26', null, null);
INSERT INTO `news_gzbd` VALUES ('473', '四川省', '5月21日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('474', '四川省', '5月20日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('475', '四川省', '5月19日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('476', '四川省', '5月18日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('477', '四川省', '5月17日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('478', '四川省', '5月16日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('479', '四川省', '5月15日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('480', '四川省', '5月14日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('481', '四川省', '5月13日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('482', '四川省', '5月12日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('483', '四川省', '5月11日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('484', '四川省', '5月10日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('485', '四川省', '5月9日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('486', '四川省', '5月8日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('487', '四川省', '5月7日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('488', '四川省', '5月6日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('489', '四川省', '5月5日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('490', '四川省', '5月4日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('491', '四川省', '5月3日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('492', '四川省', '5月2日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('493', '四川省', '5月1日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('494', '四川省', '4月30日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('495', '四川省', '4月29日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('496', '四川省', '4月28日', '561', '21', '558', '3', null, null);
INSERT INTO `news_gzbd` VALUES ('497', '四川省', '4月27日', '561', '3', '4', '24', '21', '4');
INSERT INTO `news_gzbd` VALUES ('498', '四川省', '4月26日', '561', '3', '4', '24', null, null);
INSERT INTO `news_gzbd` VALUES ('499', '四川省', '4月25日', '561', '3', '4', '24', null, null);
INSERT INTO `news_gzbd` VALUES ('500', '四川省', '4月24日', '21', null, null, null, null, null);
INSERT INTO `news_gzbd` VALUES ('501', '四川省', '4月23日', '21', null, null, null, null, null);
INSERT INTO `news_gzbd` VALUES ('502', '四川省', '4月22日', '21', '20', '1', null, null, null);
INSERT INTO `news_gzbd` VALUES ('503', '四川省', '4月21日', '21', '18', '3', null, null, null);
INSERT INTO `news_gzbd` VALUES ('504', '四川省', '4月20日', '21', '18', '3', null, null, null);
INSERT INTO `news_gzbd` VALUES ('505', '四川省', '4月19日', '21', '18', '3', null, null, null);
INSERT INTO `news_gzbd` VALUES ('506', '四川省', '4月18日', '561', '553', '3', '5', '83', null);
INSERT INTO `news_gzbd` VALUES ('507', '四川省', '4月17日', '560', '552', '3', '5', '31', null);
INSERT INTO `news_gzbd` VALUES ('508', '四川省', '4月16日', '560', '21', '552', '3', '5', '60');
INSERT INTO `news_gzbd` VALUES ('509', '四川省', '4月15日', '560', '21', '550', '3', '7', '81');
INSERT INTO `news_gzbd` VALUES ('510', '四川省', '4月14日', '560', '21', '548', '3', '9', '213');
INSERT INTO `news_gzbd` VALUES ('511', '四川省', '4月13日', '560', '21', '548', '3', '9', '216');
INSERT INTO `news_gzbd` VALUES ('512', '四川省', '4月12日', '560', '21', '547', '3', '10', '226');
