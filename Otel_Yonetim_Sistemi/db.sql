CREATE DATABASE  IF NOT EXISTS `yonetim` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `yonetim`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: yonetim
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `musteri`
--

DROP TABLE IF EXISTS `musteri`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `musteri` (
  `id` int NOT NULL,
  `ad` varchar(45) DEFAULT NULL,
  `cinsiyet` varchar(45) DEFAULT NULL,
  `tel` varchar(45) DEFAULT NULL,
  `mail` varchar(45) DEFAULT NULL,
  `uyruk` varchar(45) DEFAULT NULL,
  `tc` char(11) DEFAULT NULL,
  `adres` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `musteri`
--

LOCK TABLES `musteri` WRITE;
/*!40000 ALTER TABLE `musteri` DISABLE KEYS */;
INSERT INTO `musteri` VALUES (43,'Messi','Bay','787878','messi@gmail.com','Arjantin','87878778','ABD'),(1234,'Nurkan Özlük','Bay','4545','nurkan@gmail.com','T.C.','123456789','Türkiye'),(4444,'Lebron James','Bay','111111','lebron@gmail.com','ABD','56566','ABD'),(8888,'Michael Jordan','Bay','78787878','jordan@gmail.com','ABD','9989898','ABD');
/*!40000 ALTER TABLE `musteri` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oda`
--

DROP TABLE IF EXISTS `oda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oda` (
  `odano` int NOT NULL,
  `kat` varchar(45) DEFAULT NULL,
  `odaturu` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`odano`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oda`
--

LOCK TABLES `oda` WRITE;
/*!40000 ALTER TABLE `oda` DISABLE KEYS */;
INSERT INTO `oda` VALUES (1,'2','kkkkk'),(4343,'8888888','ererre'),(222222,'55555','kkkkk');
/*!40000 ALTER TABLE `oda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rezervasyyon`
--

DROP TABLE IF EXISTS `rezervasyyon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rezervasyyon` (
  `iletisim` varchar(45) NOT NULL,
  `giris` varchar(45) DEFAULT NULL,
  `cikis` varchar(45) DEFAULT NULL,
  `odaturu` varchar(45) DEFAULT NULL,
  `bosoda` varchar(45) DEFAULT NULL,
  `gun` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`iletisim`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rezervasyyon`
--

LOCK TABLES `rezervasyyon` WRITE;
/*!40000 ALTER TABLE `rezervasyyon` DISABLE KEYS */;
INSERT INTO `rezervasyyon` VALUES ('05324523215','07/08/2024','13/08/2024','Single','1002','6'),('05329857642','4565','566576','Suit','1006','12'),('05347897172','05/08/2024','09/08/2024','Suit','1005','4'),('333','07/08/2024','13/08/2024','Single','1001','13'),('3343434','343','33223','jujuj','2','23'),('3434','01/08/2024','06/08/2024','{Tek Kişilik}','2','4'),('4343','8888888','ererre','Suit','',''),('444','44','44','kkkkk','1','44'),('4444','34344','3434343','Single','4343','4'),('54545455','454545','454545','kkkkk','1','555');
/*!40000 ALTER TABLE `rezervasyyon` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-08 23:34:31
