-- Create the crimes table
CREATE TABLE IF NOT EXISTS crimes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT NOT NULL,
    location VARCHAR(255),
    date DATE
);

-- Create the suspects table
CREATE TABLE IF NOT EXISTS suspects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    crime_id INT,
    FOREIGN KEY (crime_id) REFERENCES crimes(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
