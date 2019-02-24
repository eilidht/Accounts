DROP TABLE IF EXISTS account;

CREATE TABLE account (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  account_name TEXT NOT NULL,
  available_balance INTEGER NOT NULL
--  TODO finish db
-- would be useful to track created and updated at too
);
