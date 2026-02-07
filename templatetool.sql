-- MySQL dump 10.13  Distrib 5.5.38, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: templatetool
-- ------------------------------------------------------
-- Server version	5.5.38-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `examlogos`
--

DROP TABLE IF EXISTS `examlogos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `examlogos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text,
  `status` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `examlogos`
--

LOCK TABLES `examlogos` WRITE;
/*!40000 ALTER TABLE `examlogos` DISABLE KEYS */;
INSERT INTO `examlogos` VALUES (1,'cci',1),(2,'ibps',1),(3,'ifsca',1),(4,'iibf',1),(5,'irdai',1),(6,'lic',1),(7,'nabard',1),(8,'niacl',1),(9,'rbi',1),(10,'rrb',1),(11,'sbi',1),(12,'sebi',1),(13,'sidbi',1),(14,'ssc',1);
/*!40000 ALTER TABLE `examlogos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facimg`
--

DROP TABLE IF EXISTS `facimg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `facimg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text,
  `status` int(11) NOT NULL DEFAULT '1',
  `category_id` int(11) NOT NULL,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facimg`
--

LOCK TABLES `facimg` WRITE;
/*!40000 ALTER TABLE `facimg` DISABLE KEYS */;
INSERT INTO `facimg` VALUES (1,'aditi',1,1,NULL),(2,'afreen',1,1,NULL),(3,'ajay',1,2,NULL),(4,'anshul',1,1,NULL),(5,'aritra',1,2,NULL),(6,'chhavi',1,1,NULL),(7,'dheerendra',1,2,NULL),(8,'prabal',1,2,NULL),(9,'payal',1,1,NULL),(10,'nikita',1,2,NULL),(11,'marut',1,1,NULL),(12,'mannat',1,2,NULL),(13,'manish',1,2,NULL),(14,'kapil',1,2,NULL),(15,'himanshu',1,2,NULL),(16,'dheerendra',1,2,NULL),(17,'pradyumna',1,2,NULL),(18,'prateek',1,1,NULL),(19,'rajeev',1,1,NULL),(20,'roshan',1,1,NULL),(21,'saba',1,2,NULL),(22,'sanjay',1,1,NULL),(23,'shahbaz',1,1,NULL),(24,'shaifali',1,2,NULL),(25,'sheetal',1,2,NULL),(26,'shefali',1,2,NULL),(27,'shubham',1,1,NULL),(28,'shubham1',1,1,NULL),(29,'srimoyi',1,2,NULL),(30,'varsha',1,2,NULL),(31,'veer',1,1,NULL),(32,'yash',1,1,NULL);
/*!40000 ALTER TABLE `facimg` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-07  2:33:40
