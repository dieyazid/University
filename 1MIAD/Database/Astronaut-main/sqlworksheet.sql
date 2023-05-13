CREATE TYPE astronaut_type AS OBJECT (
  astro_id INT,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  birthdate DATE,
  country VARCHAR(255)
);
/
CREATE TYPE astronauts_list AS TABLE OF astronaut_type;
/
CREATE TYPE mission_type AS OBJECT (
  miss_id INT,
  miss_name VARCHAR(255),
  start_date DATE,
  end_date DATE,
  destination VARCHAR(255),
  astronauts astronauts_list
);

CREATE TABLE astronaut OF astronaut_type(
    CONSTRAINT pk_astronaut PRIMARY KEY(astro_id)
);
/
CREATE TABLE mission OF mission_type (
    CONSTRAINT pk_mission PRIMARY KEY(miss_id)
)NESTED TABLE astronauts STORE AS astronauts_list1;


INSERT INTO mission (miss_id, miss_name, start_date, end_date, destination, astronauts)
VALUES (5, 'APOLO69', TO_DATE('05/01/2023', 'dd/mm/yyyy'), TO_DATE('05/01/2024', 'dd/mm/yyyy'), 'MARS',
    (SELECT CAST(MULTISET(SELECT * FROM astronaut WHERE astro_id = 16) AS astronauts_list) FROM DUAL)
);

select * from astronaut where astro_id=1
select miss_id, miss_name, start_date, end_date, destination, astronauts from mission;