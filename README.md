CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    content VARCHAR(200) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

script

DB url : postgresql://todoapp:Adcb%401234@pgdbadmin.postgres.database.azure.com:5432/tododb?sslmode=require
