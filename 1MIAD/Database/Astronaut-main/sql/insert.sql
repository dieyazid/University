INSERT INTO astronaut (astro_id, first_name, last_name, birthdate, country)VALUES (1, 'John', 'Doe', TO_DATE('01/01/1970', 'DD/MM/YYYY'), 'USA');
@
INSERT INTO astronaut (astro_id, first_name, last_name, birthdate, country)
VALUES (2, 'Yazid', 'Ben', TO_DATE('01/01/1970', 'DD/MM/YYYY'), 'ALG');
@
INSERT INTO mission (miss_id, miss_name, start_date, end_date, destination, astronauts_list)
VALUES (
  1, 
  'Mission 1', 
  TO_DATE('01/01/2022', 'DD/MM/YYYY'), 
  TO_DATE('01/02/2022', 'DD/MM/YYYY'), 
  'Moon', 
  astronaut_list_type(astronaut_type(
    1,
    'John', 
    'Doe', 
    TO_DATE('01/01/1970', 'DD/MM/YYYY'), 
    'USA')
    ,
    astronaut_type(
      2,
      'Yazid',
      'Ben',
      TO_DATE('01/01/1970', 'DD/MM/YYYY'),
      'ALG'
    )
));
