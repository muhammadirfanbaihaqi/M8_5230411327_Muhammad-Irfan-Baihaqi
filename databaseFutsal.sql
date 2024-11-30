-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for futsal
CREATE DATABASE IF NOT EXISTS `futsal` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `futsal`;

-- Dumping structure for table futsal.ms_lapangan
CREATE TABLE IF NOT EXISTS `ms_lapangan` (
  `id_lapangan` int NOT NULL AUTO_INCREMENT,
  `nama_lapangan` varchar(255) NOT NULL,
  PRIMARY KEY (`id_lapangan`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table futsal.ms_lapangan: ~3 rows (approximately)
INSERT INTO `ms_lapangan` (`id_lapangan`, `nama_lapangan`) VALUES
	(1, 'Lapangan 1'),
	(2, 'Lapangan 2'),
	(3, 'Lapangan 3');

-- Dumping structure for table futsal.ms_pembooking
CREATE TABLE IF NOT EXISTS `ms_pembooking` (
  `no_telepon` varchar(20) NOT NULL,
  `nama_pembooking` varchar(255) NOT NULL,
  PRIMARY KEY (`no_telepon`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table futsal.ms_pembooking: ~9 rows (approximately)
INSERT INTO `ms_pembooking` (`no_telepon`, `nama_pembooking`) VALUES
	('085228479111', 'muliono'),
	('089671715251', 'panpanpan'),
	('089671725329', 'Muhammad Irfan Baihaqi'),
	('0989901', 'irfanbaihaqi'),
	('0iu', 'kiero'),
	('123', 'muliani'),
	('123321', 'muliono aji'),
	('12345', 'fixer'),
	('232323', 'harimau sumatra'),
	('333222', 'wielino xd');

-- Dumping structure for table futsal.tr_daftar_booking
CREATE TABLE IF NOT EXISTS `tr_daftar_booking` (
  `id_booking` int NOT NULL AUTO_INCREMENT,
  `no_telepon` varchar(20) NOT NULL,
  `id_lapangan` int NOT NULL,
  `waktu_mulai_booking` datetime NOT NULL,
  `durasi_booking` int NOT NULL,
  `waktu_selesai_booking` datetime NOT NULL,
  `total_bayar` int DEFAULT NULL,
  PRIMARY KEY (`id_booking`),
  KEY `fk_id_lapangan` (`id_lapangan`),
  KEY `fk_no_telepon` (`no_telepon`),
  CONSTRAINT `fk_id_lapangan` FOREIGN KEY (`id_lapangan`) REFERENCES `ms_lapangan` (`id_lapangan`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table futsal.tr_daftar_booking: ~4 rows (approximately)
INSERT INTO `tr_daftar_booking` (`id_booking`, `no_telepon`, `id_lapangan`, `waktu_mulai_booking`, `durasi_booking`, `waktu_selesai_booking`, `total_bayar`) VALUES
	(22, '089671715251', 3, '2024-12-31 12:00:00', 25, '2025-01-01 12:59:59', 250000),
	(23, '0989901', 1, '2024-12-31 01:00:00', 48, '2025-01-02 00:59:59', 480000),
	(24, '089671725329', 1, '2024-11-29 22:00:00', 2, '2024-11-29 23:59:59', 20000),
	(26, '089671725329', 1, '2024-11-30 12:00:00', 3, '2024-11-30 14:59:59', 30000);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
