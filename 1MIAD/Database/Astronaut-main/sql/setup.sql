CREATE TYPE astronaut_type AS OBJECT (
  astro_id INT,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  birthdate DATE,
  country VARCHAR(255),
  id_photo BLOB
);
@
CREATE TYPE astronaut_list_type AS TABLE OF astronaut_type;
@
CREATE OR REPLACE TYPE mission_type AS OBJECT (
  miss_id INT,
  miss_name VARCHAR(255),
  start_date DATE,
  end_date DATE,
  destination VARCHAR(255),
  astronauts_list astronaut_list_type
);
@
CREATE TABLE astronaut OF astronaut_type(
    CONSTRAINT pk_astronaut PRIMARY KEY(astro_id)
);
@
CREATE TABLE mission OF mission_type (
    CONSTRAINT pk_mission PRIMARY KEY(miss_id)
)NESTED TABLE astronauts_list STORE AS astronaut_ids_list1;
@
