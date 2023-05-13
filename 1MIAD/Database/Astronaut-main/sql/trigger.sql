CREATE OR REPLACE TRIGGER CHECK_ASTRONAUTS
AFTER INSERT OR UPDATE ON mission
FOR EACH ROW
DECLARE
  l_count INTEGER;
BEGIN
    FOR i IN 1 .. :new.astronauts_list.COUNT LOOP
        SELECT COUNT(1) INTO l_count FROM astronaut WHERE astro_id = :new.astronauts_list(i).astro_id;
        IF l_count=0 THEN
            RAISE_APPLICATION_ERROR(-20000, 'Astronaut with astro_id ' || :new.astronauts_list(i).astro_id || ' does not exist in astronaut table');
        END IF;
    END LOOP;
END;
/
@