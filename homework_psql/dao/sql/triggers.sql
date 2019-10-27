
CREATE OR REPLACE PACKAGE orm_owner_cars IS


    TYPE car_data IS RECORD(
        car_number ORM_CAR.CAR_NUMBER%TYPE,
        cars_count INTEGER
    );


    TYPE tblcardata IS TABLE OF car_data;

    FUNCTION GetCarData (car_number ORM_CAR.CAR_NUMBER%TYPE default null)
        RETURN tblskilldata
        PIPELINED;

END orm_owner_cars;

CREATE OR REPLACE PACKAGE BODY orm_owner_cars IS

    FUNCTION GetCarData (car_number ORM_CAR.CAR_NUMBER%TYPE default null)
        RETURN tblskilldata
        PIPELINED
    IS

        TYPE car_cursor_type IS REF CURSOR;
        car_cursor  car_cursor_type;

        cursor_data car_data;
        query_str varchar2(1000);

    begin

        query_str :='select ORM_OWNER_CAR.car_number, count(ORM_OWNER_CAR.car_number)
                        from ORM_OWNER_CAR ';

        -- optional part where
            if car_number is not null then
             query_str:= query_str||' where trim(ORM_OWNER_CAR.car_number) = trim('''||car_number||''') ';
            end if;
        -- end optional part

        query_str := query_str||' group by ORM_OWNER_CAR.car_number';



        OPEN car_cursor FOR query_str;
        LOOP
            FETCH car_cursor into cursor_data;
            exit when (skill_cursor %NOTFOUND);

            PIPE ROW (cursor_data);

        END LOOP;


    END GetCarData;

END orm_owner_cars;