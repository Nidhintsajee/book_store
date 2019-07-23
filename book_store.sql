-- phpMyAdmin SQL Dump
-- version 4.7.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 21, 2019 at 04:48 PM
-- Server version: 5.7.16-log
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `book_store`
--

-- --------------------------------------------------------

--
-- Table structure for table `author`
--

CREATE TABLE `author` (
  `A_ID` int(11) NOT NULL,
  `A_FNAME` varchar(50) DEFAULT NULL,
  `A_LNAME` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `author`
--

INSERT INTO `author` (`A_ID`, `A_FNAME`, `A_LNAME`) VALUES
(1, 'Marcel', 'Proust'),
(2, 'Miguel de', 'Cervantes'),
(3, 'James', 'Joyce'),
(4, 'F. Scott', 'Fitzgerald'),
(5, 'James', 'Joyce'),
(6, 'Herman', 'Melville'),
(7, 'J. K. ', 'Rowling');

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `B_ID` int(11) NOT NULL,
  `B_TITLE` varchar(50) DEFAULT NULL,
  `B_A_ID` int(11) DEFAULT NULL,
  `B_PUBLISHER` varchar(50) DEFAULT NULL,
  `B_PUB_DATE` datetime DEFAULT NULL,
  `B_SUBJECT` varchar(50) DEFAULT NULL,
  `B_UNIT_PRICE` float DEFAULT NULL,
  `B_STOCK` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`B_ID`, `B_TITLE`, `B_A_ID`, `B_PUBLISHER`, `B_PUB_DATE`, `B_SUBJECT`, `B_UNIT_PRICE`, `B_STOCK`) VALUES
(1, 'TITLE 1', 1, 'asfasf', '1997-06-26 00:00:00', 'afjkhkd asjkghf ashkgf dfg', 1800, 2000);

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `C_ID` varchar(10) NOT NULL,
  `C_NAME` varchar(50) DEFAULT NULL,
  `C_ADD` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`C_ID`, `C_NAME`, `C_ADD`) VALUES
('C-0001', 'Faraz', 'Address of Faraz, at House and city');

-- --------------------------------------------------------

--
-- Table structure for table `reservation`
--

CREATE TABLE `reservation` (
  `R_ID` int(11) NOT NULL,
  `R_C_ID` int(11) DEFAULT NULL,
  `R_C_NAME` varchar(50) DEFAULT NULL,
  `R_B_ID` int(11) DEFAULT NULL,
  `R_B_TITLE` varchar(50) DEFAULT NULL,
  `R_B_QUANTITY` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `author`
--
ALTER TABLE `author`
  ADD PRIMARY KEY (`A_ID`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`B_ID`),
  ADD KEY `fk_books_author` (`B_A_ID`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`C_ID`);

--
-- Indexes for table `reservation`
--
ALTER TABLE `reservation`
  ADD PRIMARY KEY (`R_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `author`
--
ALTER TABLE `author`
  MODIFY `A_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `B_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `reservation`
--
ALTER TABLE `reservation`
  MODIFY `R_ID` int(11) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `books`
--
ALTER TABLE `books`
  ADD CONSTRAINT `fk_books_author` FOREIGN KEY (`B_A_ID`) REFERENCES `author` (`A_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
