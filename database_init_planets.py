import sqlite3

# this is the database initialization file
# run this file if you want to reset/initialize the planet database

def database_init_planets():

    # database file connection
    database = sqlite3.connect("Database")

    # cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers
    cursor = database.cursor()

    #This unit will drop the planet table
    sql_command = """
    DROP TABLE IF EXISTS PLANET;"""
    cursor.execute(sql_command)
    ######################################################################
    # SQL command to create a table in the database
    sql_command = """CREATE TABLE IF NOT EXISTS PLANET (
    Name 		    TEXT 	PRIMARY KEY 	NOT NULL,
    Mass            REAL,
    Semimajoraxis   REAL,
    Eccentricity    REAL,
    Periapsis       REAL,
    Period          REAL,
    Inclination     REAL,
    Ascending_node  REAL,
    Perihelion      REAL,
    Baseangle       REAL
    )
    ;"""

    # execute the statement1

    cursor.execute(sql_command)
    #Template for inserting into the database
    # INSERT INTO PLANET VALUES('Name', mass, semiMajorAxis, eccentricity, periapsis, period, Inclination, AscendingNode, Perihelion, baseAngle);

    cursor.execute("""
    INSERT INTO PLANET VALUES('Earth',  (5.972*1000000000000000000000000),	149598262,	0.017,	147098291, 365.25636, 0, -0.196535244, 1.796767421, 1.749518042);
    """)
    cursor.execute("""
    INSERT INTO PLANET VALUES('Mercury', .33*1000000000000000000000000, 57909227, 0.206, 46001009, 87.95373149, 0.122173048, 0.843546774, 1.351870079, 3.936939194);
    """)




    # QUERY FOR ALL
    # print("ENTIRE DATA BASE\nPLANETS:")
    # cursor.execute("""SELECT * FROM PLANET""")
    # query_result = cursor.fetchall()
    #
    # for i in query_result:
    #     print(i)


    # To save the changes in the files. Never skip this.
    # If we skip this, nothing will be saved in the database.
    database.commit()
    # close the connection
    database.close()
