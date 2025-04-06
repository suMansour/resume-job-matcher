-- jobs table
CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    location TEXT,
    company TEXT,
    skills TEXT[],
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);