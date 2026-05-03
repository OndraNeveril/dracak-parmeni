DROP TABLE IF EXISTS items;

CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    value INTEGER
);

INSERT INTO items VALUES
(1, 'Pařmen', 'Dojdi s Fritolem na pařbu do Naadoru', 0),
(2, 'Šourek. Fritol Šourek', 'Úspěšně projdi celou konverzaci na styl Jamese Bonda', 0),
(3, 'Abstinent', 'Dokonči celou hru, aniž bys vypil pivo či okenu a vyhulil čmoudovou trávu', 0),
(4, 'Diplomat', 'Přesvědč Elbonda, aby s tebou šel na pařbu', 0),
(5, 'Devítka', 'Dojdi na pařbu spolu se všemi originálními pařmeny', 0),
(6, 'Opička', 'Ochoč si chlupa', 0);
