SELECT * FROM users;
SELECT * FROM items;
INSERT INTO items (item) VALUE("car"),("rolex"),("vacation"),("mountain bike"),("mac pro"),("hiking bag"),("bbq grill"),("zumba dvd"),("samsung watch"),("3 cats"),("A house of cats");
INSERT INTO items (item) VALUE("water bed"),("diamond neckalce"),("nike sports shoe"),("iPhone"),("galaxy note 22 ultra"),("a baby");
INSERT INTO users (name,username) VALUES ("derick", "dparr1"), ("kayla","klop123");

SELECT * FROM items 
LEFT JOIN users_and_items ON items.id = users_and_items.item_id 
LEFT JOIN users ON users.id = users_and_items.user_id
WHERE users.id <> 14
AND items.id NOT IN (
	SELECT items.id FROM items 
	LEFT JOIN users_and_items ON items.id = users_and_items.item_id 
	LEFT JOIN users ON users.id = users_and_items.user_id
	WHERE users.id = 14
);

SELECT * FROM items 
LEFT JOIN users_and_items ON items.id = users_and_items.item_id 
LEFT JOIN users ON users.id = users_and_items.user_id
WHERE items.id = 73;
SELECT * FROM users JOIN users_and_items ON users.id = users_and_items.user_id JOIN items ON items.id = users_and_items.item_id WHERE users.id = "7";

SELECT * FROM users JOIN users_and_items ON users.id = users_and_items.user_id JOIN items ON items.id = users_and_items.item_id WHERE users.id = "12";

SELECT *
FROM users
JOIN items
ON users.user_id = items.id
WHERE users.user_id = '1';

SELECT * FROM users_and_items;
INSERT INTO items(item,added_by) VALUES("vacation", "Jake");