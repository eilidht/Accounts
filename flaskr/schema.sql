DROP TABLE IF EXISTS account;

CREATE TABLE account(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  account_name TEXT,
  account_nickname TEXT,
  account_owner_name TEXT NOT NULL,
  account_type TEXT NOT NULL,
  currency TEXT NOT NULL,
  available_balance INTEGER NOT NULL DEFAULT 0,
  booked_balance INTEGER NOT NULL DEFAULT 0,
  status TEXT NOT NULL DEFAULT 'open'
-- would be useful to track created and updated at too
);
