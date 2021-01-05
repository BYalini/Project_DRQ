DROP DATABASE IF EXISTS `yalinidatarepresentation`;
CREATE DATABASE `yalinidatarepresentation`;
USE `yalinidatarepresentation`;

DROP TABLE IF EXISTS `cars`;
CREATE TABLE `car` (
  `registration` varchar(15) NOT NULL,
  `make` varchar(20) DEFAULT NULL,
  `model` varchar(20) DEFAULT NULL,
  `colour` varchar(10) DEFAULT NULL,
  `mileage` int(11) DEFAULT NULL,
  `engineSize` float(2,1) DEFAULT NULL,
  PRIMARY KEY (`registration`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `person` (
  `personID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `age` int(11) DEFAULT NULL,
  `sex` enum('M','F') DEFAULT 'M',
  `cregistration` varchar(20) DEFAULT NULL,
  `isStudent` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`personID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

INSERT INTO `car` VALUES ('05-MO-17931','Toyota','Highlander','Green',253789,1.6),('10-G-2334','Toyota','Corolla','Green',123389,1.3);
INSERT INTO `person` VALUES (1,'John',23,'M','11-MO-23431',1),(2,'Tom',64,'M','132-G-9923',0),(3,'Mary',12,'F','132-MO-19323',1);