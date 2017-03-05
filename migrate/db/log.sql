create table log(
	generation  int not null,
	step        int not null,
	field       json,
	logdatetime timestamp not null,
	primary key (generation, step)
);
