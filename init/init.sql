CREATE TABLE my_table (
                          id SERIAL PRIMARY KEY,
                          name TEXT,
                          income INT,
                          education_years INT,
                          age INT
);

INSERT INTO my_table (name, income, education_years, age) VALUES
                      ('Alice', 50000, 16, 30),
                      ('Bob', 60000, 14, NULL),
                      ('Charlie', 55000, 18, 35),
                      ('David', 40000, 12, NULL),
                      ('Eva', 75000, 20, 40);
