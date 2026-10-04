CREATE DATABASE db_gestion_escolar;
CREATE USER 'admin_escolar'@'%' IDENTIFIED BY 'inacap123';
GRANT ALL PRIVILEGES ON db_gestion_escolar.* TO 'admin_escolar'@'%';
FLUSH PRIVILEGES;