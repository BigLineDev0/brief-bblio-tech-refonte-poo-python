CREATE DATABASE bibliotheque;
USE bibliotheque;

CREATE TABLE catalogues (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(100) not null,
    auteur VARCHAR(100) not null,
    type ENUM("LIVRE", "MAGAZINE"),
    frequence varchar(100),
    disponible BOOLEAN DEFAULT TRUE
);



CREATE TABLE adherants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) not null
);

CREATE TABLE emprunts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_adherant INT,
    id_catalogue INT,
    date_emprunt datetime  DEFAULT CURRENT_TIMESTAMP,
    date_retour_programme datetime,
    date_retour datetime,
    status Enum("Emprunte", "Restitue") DEFAULT 'Emprunte',
    FOREIGN KEY (id_adherant) REFERENCES adherants(id),
    FOREIGN KEY (id_catalogue) REFERENCES catalogues(id)
)


CREATE TABLE utilisateurs(
    id int PRIMARY KEY AUTO_INCREMENT,
    nom varchar(100) not null,
    prenom varchar(100) not null,
    email varchar(100) unique not null ,
    password varchar(100) unique not null,
    role enum("admin", "user") DEFAULT "admin"
);



SELECT a.nom , c.titre, e.date_emprunt, e.date_retour_programme from adherants as a 
join emprunts as e on e.id_adherant=a.id 
join catalogues as c on e.id_catalogue=c.id;