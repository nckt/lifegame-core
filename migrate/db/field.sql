create table field(
	generation int not null,
	step       int not null,
	field      json,
	check(count(*) <= 1)
);

CREATE OR REPLACE FUNCTION trg_field_ins()
	RETURNS "trigger" AS
$BODY$
declare
begin
	insert into log (
		generation,
		step,
		field,
		logdatetime
	) values (
		new.generation,
		new.step,
		new.field,
		clock_timestamp()
	);
end;
$BODY$
LANGUAGE plpgsql VOLATILE;

CREATE TRIGGER trg_field_ins
AFTER INSERT ON accounts
FOR EACH ROW
EXECUTE PROCEDURE trg_field_ins();

