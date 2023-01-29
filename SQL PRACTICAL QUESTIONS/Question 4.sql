-- Creating Table 1: Vehicles
CREATE TABLE Vehicles (
    Make VARCHAR(255) NOT NULL,
    Model VARCHAR(255) NOT NULL,
    Manufacture_Date DATE NOT NULL,
    Cost DECIMAL(10, 2) NOT NULL,
    Model_id INT NOT NULL,
    PRIMARY KEY (Model_id),
    CHECK (Model_id > 0)
);
ALTER TABLE Vehicles ADD CONSTRAINT chk_row_count CHECK ( (SELECT COUNT(*) FROM Vehicles) <= 5);

-- Creating Table 2: Manufacturers
CREATE TABLE Manufacturers (
    Manufacturer VARCHAR(255) NOT NULL,
    Model_id INT NOT NULL,
    Parts VARCHAR(255) NOT NULL,
    Warranty_Expiry_Date DATE NOT NULL,
    City VARCHAR(255) NOT NULL,
    FOREIGN KEY (Model_id) REFERENCES Vehicles(Model_id)
);
ALTER TABLE Manufacturers ADD CONSTRAINT chk_row_count CHECK ( (SELECT COUNT(*) FROM Manufacturers) <= 5);

-- Populating Table 1: Vehicles
INSERT INTO Vehicles (Make, Model, Manufacture_Date, Cost, Model_id)
VALUES ('BMW', 'M4', '2023-01-01', 25000, 1),
       ('Mercedes', 'AMG', '2023-01-02', 22000, 2),
       ('Toyota', 'Corolla', '2023-01-03', 35000, 3);

-- Populating Table 2: Manufacturers
INSERT INTO Manufacturers (Manufacturer, Model_id, Parts, Warranty_Expiry_Date, City)
VALUES ('BMW', 1, 'Engine, Transmission, Suspension', '2025-01-01', 'Johannesburg'),
       ('Mercedes', 2, 'Engine, Transmission, Suspension', '2025-01-02', 'Cape Town'),
       ('Toyota', 3, 'Engine, Transmission, Suspension', '2025-01-03', 'Durban');
