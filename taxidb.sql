-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 04, 2018 at 07:16 PM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `taxidb`
--

-- --------------------------------------------------------

--
-- Table structure for table `log`
--

CREATE TABLE `log` (
  `timestamp` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `seats` int(2) NOT NULL,
  `taxino` varchar(255) NOT NULL,
  `driver` varchar(255) NOT NULL,
  `mode` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `log`
--

INSERT INTO `log` (`timestamp`, `name`, `location`, `seats`, `taxino`, `driver`, `mode`) VALUES
('22:39|4 4 2018', 'Adith', 'BTM', 1, 'KA 01 ET 2000', 'Amith', 'p'),
('22:39|4 4 2018', 'Sankarsh', 'BTM', 1, 'KA 01 ET 2000', 'Amith', 'p'),
('22:43|4 4 2018', 'Adith', 'BSK', 1, 'KA 01 ET 2000', 'Amith', 'p');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `driver` varchar(255) NOT NULL,
  `taxino` varchar(255) NOT NULL,
  `availability` int(2) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`driver`, `taxino`, `availability`) VALUES
('Suresh', 'KA 05 MD 9450', 1),
('Amith', 'KA 01 ET 2000', 0),
('Sankarsh', 'KA 05 MD 3243', 0),
('Ramu', 'KA 05 MD 5197', 1);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`username`, `password`) VALUES
('Adith', 'Password123'),
('Sankarsh', 'Dam123'),
('Sammy', 'Sam123');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
