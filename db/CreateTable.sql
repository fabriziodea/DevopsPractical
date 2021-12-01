CREATE TABLE IF NOT EXISTS winners
            (  
                    raceno INTEGER NOT NULL AUTO_INCREMENT,
                    name    VARCHAR(30) NOT NULL,
                    PRIMARY KEY (raceno)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


LOCK TABLES `winners` WRITE;
/*!40000 ALTER TABLE `winners` DISABLE KEYS */;
INSERT INTO `winners` VALUES (1,'Legacy winner Donkey');
/*!40000 ALTER TABLE `winners` ENABLE KEYS */;
UNLOCK TABLES;

