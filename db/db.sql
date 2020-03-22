-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: hacka
-- ------------------------------------------------------
-- Server version       5.7.29-0ubuntu0.18.04.1

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
-- Table structure for table `tbl_deliveries`
--

DROP TABLE IF EXISTS `tbl_deliveries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_deliveries` (
  `deliveryid` int(11) NOT NULL AUTO_INCREMENT,
  `fk_supplyid` int(11) NOT NULL,
  `fk_demandid` int(11) NOT NULL,
  `fk_supplier` int(11) NOT NULL,
  `fk_demander` int(11) NOT NULL,
  PRIMARY KEY (`deliveryid`),
  KEY `fk_supplyid_idx` (`fk_supplyid`),
  KEY `fk_demandid_idx` (`fk_demandid`),
  KEY `fk_supplierid_idx` (`fk_supplier`),
  KEY `fk_demanderid_idx` (`fk_demander`),
  CONSTRAINT `fk_demanderid` FOREIGN KEY (`fk_demander`) REFERENCES `tbl_institutions` (`institutionid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_demandid` FOREIGN KEY (`fk_demandid`) REFERENCES `tbl_demand` (`demandid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_supplierid` FOREIGN KEY (`fk_supplier`) REFERENCES `tbl_institutions` (`institutionid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_supplyid` FOREIGN KEY (`fk_supplyid`) REFERENCES `tbl_supply` (`supplyid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_deliveries`
--

LOCK TABLES `tbl_deliveries` WRITE;
/*!40000 ALTER TABLE `tbl_deliveries` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_deliveries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_demand`
--

DROP TABLE IF EXISTS `tbl_demand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_demand` (
  `demandid` int(11) NOT NULL AUTO_INCREMENT,
  `fk_institutionid` int(11) NOT NULL,
  `objecttype` varchar(200) NOT NULL,
  `amount` int(20) NOT NULL,
  PRIMARY KEY (`demandid`),
  KEY `fk_institutionid_idx` (`fk_institutionid`),
  CONSTRAINT `fk_institutionid` FOREIGN KEY (`fk_institutionid`) REFERENCES `tbl_institutions` (`institutionid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_demand`
--

LOCK TABLES `tbl_demand` WRITE;
/*!40000 ALTER TABLE `tbl_demand` DISABLE KEYS */;
INSERT INTO `tbl_demand` VALUES (1,1,'disinfectant',100),(2,1,'gloves',100),(3,1,'masks',100),(4,3,'masks',150),(5,4,'masks',70),(7,2,'masks',80),(8,5,'masks',40),(10,5,'masks',40),(11,5,'masks',40),(12,2,'disinfectant',30),(13,4,'disinfectant',70),(15,1,'masks',160),(16,3,'masks',650),(17,4,'masks',3000),(18,6,'masks',500);
/*!40000 ALTER TABLE `tbl_demand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_institutions`
--

DROP TABLE IF EXISTS `tbl_institutions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_institutions` (
  `institutionid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) NOT NULL,
  `type` varchar(100) NOT NULL,
  `address` varchar(300) NOT NULL,
  `contact` varchar(200) NOT NULL,
  `telephone` varchar(45) NOT NULL,
  `lat` float DEFAULT NULL,
  `lng` float DEFAULT NULL,
  PRIMARY KEY (`institutionid`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_institutions`
--

LOCK TABLES `tbl_institutions` WRITE;
/*!40000 ALTER TABLE `tbl_institutions` DISABLE KEYS */;
INSERT INTO `tbl_institutions` VALUES (1,'Asklepios Krankenhaus St. Georg','medical','Lohmühlenstraße 5, 20099 Hamburg','Robert Pirsig','012345698',53.5526,10.0186),(2,'Facharztpraxis für Pneumologie und Gynäkologie | St. Georg','medical','Steindamm 32, 20099 Hamburg','Jan Tiesto','01237888',53.5537,10.0128),(3,'Gesundheitszentrum Dr. Dr. Müller und Kollegen AG','medical','Kurze Mühren 6, 20095 Hamburg','Max Mustermann','01237898',53.553,10.0036),(4,'Dr. med. Paul Schulz prakt. Arzt','medical','Grootsruhe 2, 20537 Hamburg','Meg Whitmann','0126788898',53.5551,10.0425),(5,'Gemeinschaftspraxis für Allgemeinmedizin - Dr. Olaf Feuer; Cornelia Traub; Dr. Eda Siebke','medical','Hein-Köllisch-Platz 1, 20359 Hamburg','Boris Johnson','0694206969',53.5477,9.95751),(6,'Gemeinschaftspraxis für Allgemeinmedizin Hamburg','medical','Clemens-Schultz-Straße 90, 20359 Hamburg','Emma Goldman','012346009',53.5524,9.96396),(8,'Hebammenpraxis Hamburg','medical','Armbruststraße 9, 20257 Hamburg','Ash Ketchum','012345449',53.575,9.94274),(9,'G.U.A.R.D. Rettungswache Hamburg Nord','medical','Alfredstraße 9, 22087 Hamburg','Julian Assange','0143456749',53.5931,10.0077),(10,'Seniorenhaus Christophorus','medical','Maria-Louisen-Straße 30, 22301 Hamburg','Gordan Ramsey','012347849',53.5597,10.0088),(11,'Ärtztehaus Hamburg Seitenstr.','medical','Schulweg 12, 17649 Teltow ','Albert Hoffmann','1234',53.567,10.0077),(12,'FINEXITY AG','company','Holzdamm 28-32, 20099 Hamburg','Jean-Paul Satre','01444567749',53.5559,10.0056),(13,'Artzt Praxis Dr. Fiktiv.','medical','Schulweg 12, 17649 Teltow ','Albert Hoffmann','1234',53.5589,10.0056),(14,'Goethe-Institut Hamburg Sprachschule Deutschkurse','company','Hühnerposten 1, 20097 Hamburg','Ken Kesey','01444567749',53.549,10.0084),(15,'Heinrich-Wolgast-Schule','company','Greifswalder Str. 40, 20099 Hamburg','DT Suzuki','0144452314329',53.5559,10.0118),(16,'Hamburger Volksbank eG','company','Rosenstraße 2, 20095 Hamburg','Rosa Parks','01444456329',53.5533,10.0014);
/*!40000 ALTER TABLE `tbl_institutions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_supply`
--

DROP TABLE IF EXISTS `tbl_supply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_supply` (
  `supplyid` int(11) NOT NULL AUTO_INCREMENT,
  `fk_institutionid` int(11) NOT NULL,
  `objecttype` varchar(200) NOT NULL,
  `amount` int(20) NOT NULL,
  PRIMARY KEY (`supplyid`),
  KEY `fk_insitutionid_idx` (`fk_institutionid`),
  CONSTRAINT `fk_insitutionid` FOREIGN KEY (`fk_institutionid`) REFERENCES `tbl_institutions` (`institutionid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_supply`
--

LOCK TABLES `tbl_supply` WRITE;
/*!40000 ALTER TABLE `tbl_supply` DISABLE KEYS */;
INSERT INTO `tbl_supply` VALUES (1,11,'masks',500),(2,12,'masks',50),(3,12,'disinfectant',500),(4,13,'disinfectant',600),(5,14,'disinfectant',750),(6,13,'masks',100),(7,14,'masks',50);
/*!40000 ALTER TABLE `tbl_supply` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-22 20:06:23