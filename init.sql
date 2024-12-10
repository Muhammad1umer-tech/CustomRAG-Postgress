CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    question_text TEXT NOT NULL,
    answer_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COPY questions(question_text, answer_text)
FROM '/docker-entrypoint-initdb.d/questions.csv'
DELIMITER ','
CSV HEADER;
