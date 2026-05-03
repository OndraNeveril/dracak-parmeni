DROP TABLE IF EXISTS items;

CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    value INTEGER
);

INSERT INTO items VALUES
(1, 'Achievement 1', 'Popis 1', 0),
(2, 'Achievement 2', 'Popis 2', 0),
(3, 'Achievement 3', 'Popis 3', 0);
