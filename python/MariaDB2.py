import os

try:
    from sqlalchemy import create_engine, text
    from sqlalchemy.exc import SQLAlchemyError
except ImportError:
    os.system("pip install sqlalchemy pymysql mariadb")
    from sqlalchemy import create_engine, text
    from sqlalchemy.exc import SQLAlchemyError
finally:
    print("All modules are imported successfully")

hostname = "<$hostname>"
database = "<$database>"
port = "<$port>"
username = "<$user>"
password = "<$password>"

connection_url = f"mariadb+mariadbconnector://{username}:{password}@{hostname}:{port}/{database}"

try:
    engine = create_engine(connection_url)

    with engine.connect() as connection:
        result = connection.execute(text("SELECT VERSION()"))
        db_info = result.fetchone()
        print("Connected to MariaDB Server version ", db_info[0])

        result = connection.execute(text("SELECT DATABASE()"))
        current_db = result.fetchone()
        print("You're connected to database: ", current_db[0])

except SQLAlchemyError as e:
    print("Error while connecting to MariaDB", e)
finally:
    if engine:
        engine.dispose()
        print("MariaDB connection is closed")
