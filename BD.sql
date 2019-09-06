CREATE TABLE `tarefas` (
  `descricao` varchar(100) NOT NULL,
  `prioridade` int(11) NOT NULL,
  `data` datetime NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `concluido` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8