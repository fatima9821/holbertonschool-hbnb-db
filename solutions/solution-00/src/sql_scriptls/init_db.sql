CREATE TABLE User (
    id VARCHAR(36) PRIMARY KEY,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Place (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    description TEXT,
    city_id VARCHAR(36) NOT NULL,
    host_id VARCHAR(36) NOT NULL,
    price_per_night INTEGER NOT NULL,
    number_of_rooms INTEGER NOT NULL,
    number_of_bathrooms INTEGER NOT NULL,
    max_guests INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES City(id),
    FOREIGN KEY (host_id) REFERENCES User(id)
);

CREATE TABLE Country (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    description TEXT,
    city_id VARCHAR(36) NOT NULL,
    host_id VARCHAR(36) NOT NULL,
    price_per_night INTEGER NOT NULL,
    number_of_rooms INTEGER NOT NULL,
    number_of_bathrooms INTEGER NOT NULL,
    max_guests INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES City(id),
    FOREIGN KEY (host_id) REFERENCES User(id)

CREATE TABLE City (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    description TEXT,
    city_id VARCHAR(36) NOT NULL,
    host_id VARCHAR(36) NOT NULL,
    price_per_night INTEGER NOT NULL,
    number_of_rooms INTEGER NOT NULL,
    number_of_bathrooms INTEGER NOT NULL,
    max_guests INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES City(id),
    FOREIGN KEY (host_id) REFERENCES User(id)

CREATE TABLE Amenity (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    description TEXT,
    city_id VARCHAR(36) NOT NULL,
    host_id VARCHAR(36) NOT NULL,
    price_per_night INTEGER NOT NULL,
    number_of_rooms INTEGER NOT NULL,
    number_of_bathrooms INTEGER NOT NULL,
    max_guests INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES City(id),
    FOREIGN KEY (host_id) REFERENCES User(id)

CREATE TABLE Review (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    description TEXT,
    city_id VARCHAR(36) NOT NULL,
    host_id VARCHAR(36) NOT NULL,
    price_per_night INTEGER NOT NULL,
    number_of_rooms INTEGER NOT NULL,
    number_of_bathrooms INTEGER NOT NULL,
    max_guests INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES City(id),
    FOREIGN KEY (host_id) REFERENCES User(id)

CREATE TABLE Place_amenity (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    description TEXT,
    city_id VARCHAR(36) NOT NULL,
    host_id VARCHAR(36) NOT NULL,
    price_per_night INTEGER NOT NULL,
    number_of_rooms INTEGER NOT NULL,
    number_of_bathrooms INTEGER NOT NULL,
    max_guests INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES City(id),
    FOREIGN KEY (host_id) REFERENCES User(id)

CREATE TABLE State (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    description TEXT,
    city_id VARCHAR(36) NOT NULL,
    host_id VARCHAR(36) NOT NULL,
    price_per_night INTEGER NOT NULL,
    number_of_rooms INTEGER NOT NULL,
    number_of_bathrooms INTEGER NOT NULL,
    max_guests INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES City(id),
    FOREIGN KEY (host_id) REFERENCES User(id)

CREATE TABLE Base (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    description TEXT,
    city_id VARCHAR(36) NOT NULL,
    host_id VARCHAR(36) NOT NULL,
    price_per_night INTEGER NOT NULL,
    number_of_rooms INTEGER NOT NULL,
    number_of_bathrooms INTEGER NOT NULL,
    max_guests INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES City(id),
    FOREIGN KEY (host_id) REFERENCES User(id)

CREATE TABLE Base_model (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    description TEXT,
    city_id VARCHAR(36) NOT NULL,
    host_id VARCHAR(36) NOT NULL,
    price_per_night INTEGER NOT NULL,
    number_of_rooms INTEGER NOT NULL,
    number_of_bathrooms INTEGER NOT NULL,
    max_guests INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES City(id),
    FOREIGN KEY (host_id) REFERENCES User(id)
INSERT INTO User (id, email, password, is_admin) VALUES ('1', 'admin@example.com', 'hashed_password', TRUE);

