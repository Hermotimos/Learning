
CREATE DATABASE example_db;


CREATE TABLE mytable (
	id INT,
	name TEXT
);

CREATE OR REPLACE FUNCTION my_trigger_func() RETURNS TRIGGER AS $PLPGSQL$
BEGIN
	PERFORM pg_notify('my_channel', '(' || NEW.id::TEXT || ', ' || NEW.name || ')');
	RETURN NULL; -- in row-level AFTER trigger it can return NULL
END;
$PLPGSQL$ LANGUAGE plpgsql;


CREATE TRIGGER my_trigger
	AFTER INSERT ON mytable
	FOR EACH ROW
	WHEN (NEW.name != 'some value')
	EXECUTE FUNCTION my_trigger_func();


-- call when client is already listening
INSERT INTO mytable
	SELECT num, 'name-' || num
	FROM generate_series(1, 14) AS num;
