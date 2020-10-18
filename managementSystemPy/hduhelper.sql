-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2020-10-18 16:29:10
-- 服务器版本： 5.7.26
-- PHP 版本： 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `hduhelper`
--

-- --------------------------------------------------------

--
-- 表的结构 `task1`
--

CREATE TABLE `task1` (
  `uid` int(11) NOT NULL,
  `name` text COLLATE utf8_unicode_ci NOT NULL,
  `building` int(11) NOT NULL,
  `room` int(11) NOT NULL,
  `bed` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `task1`
--

INSERT INTO `task1` (`uid`, `name`, `building`, `room`, `bed`) VALUES
(20322230, '杨成锴', 27, 624, 4),
(20322232, '李四', 27, 625, 2),
(20322231, '张三', 27, 624, 1);

-- --------------------------------------------------------

--
-- 表的结构 `task1_work`
--

CREATE TABLE `task1_work` (
  `building` int(11) NOT NULL COMMENT '寝室楼号',
  `room` int(11) NOT NULL COMMENT '寝室房间号',
  `1` int(11) NOT NULL COMMENT '值日顺序',
  `2` int(11) NOT NULL COMMENT '值日顺序',
  `3` int(11) NOT NULL COMMENT '值日顺序',
  `4` int(11) NOT NULL COMMENT '值日顺序',
  `5` int(11) NOT NULL COMMENT '值日顺序'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='值日顺序表';

--
-- 转存表中的数据 `task1_work`
--

INSERT INTO `task1_work` (`building`, `room`, `1`, `2`, `3`, `4`, `5`) VALUES
(27, 624, 20322230, 20322231, 20322232, 20322233, 20322234),
(27, 625, 20322230, 20322231, 20322232, 20322233, 20322234),
(27, 626, 20322230, 20322231, 20322232, 20322233, 20322234);

--
-- 转储表的索引
--

--
-- 表的索引 `task1`
--
ALTER TABLE `task1`
  ADD UNIQUE KEY `uid` (`uid`);

--
-- 表的索引 `task1_work`
--
ALTER TABLE `task1_work`
  ADD UNIQUE KEY `building` (`building`,`room`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
