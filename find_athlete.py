from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
import sys
from datetime import datetime

DB_PATH = "sqlite:///" + sys.argv[1]
Base = declarative_base()

class User(Base):

    __tablename__ = "user"

    id = sa.Column(sa.INTEGER, primary_key=True) 
    first_name = sa.Column(sa.TEXT)
    last_name = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    email = sa.Column(sa.TEXT)
    birthdate = sa.Column(sa.TEXT)
    height = sa.Column(sa.FLOAT)

class Athelete(Base):

    __tablename__ = "athelete"

    id = sa.Column(sa.INTEGER, primary_key=True) 
    age = sa.Column(sa.INTEGER)
    birthdate = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    height = sa.Column(sa.FLOAT)
    name = sa.Column(sa.TEXT)
    weight = sa.Column(sa.INTEGER)
    gold_medals = sa.Column(sa.INTEGER)
    silver_medals = sa.Column(sa.INTEGER)
    bronze_medals = sa.Column(sa.INTEGER)
    total_medals = sa.Column(sa.INTEGER)
    sport = sa.Column(sa.TEXT)
    country = sa.Column(sa.TEXT)

def connect_db():

    engine = sa.create_engine(DB_PATH)
    Sessions = sessionmaker(engine)
    session = Sessions()
    return session

def request_data():

    print("Поиск атлетов")
    user_id = input("Введите ID пользователя(Например, 13): ")
    
    return user_id

def find_bd(user, session):
    
    all_athl = session.query(Athelete).all()
    id_athls = {}

    for athl in all_athl:
        birthday = str_to_date(athl.birthdate)
        id_athls[athl.id] = birthday

    user_birthday = str_to_date(user.birthdate)
    nearest = ""
    athl_id = ""
    athl_birthday = ""

    for id_athl, birthday_athl in id_athls.items():
        nearest_abs = abs(user_birthday - birthday_athl)
        if not nearest or nearest_abs < nearest:
            nearest =nearest_abs
            athl_id = id_athl
            athl_birthday = birthday_athl
    return athl_id, athl_birthday

def find_height(user, session):
     
    all_athl = session.query(Athelete).all()
    id_athls = {}

    for athl in all_athl:
        if athl.height:
            id_athls[athl.id] = athl.height

    user_heigth = user.height
    nearest = ""
    athl_id = ""
    athl_heigth = ""

    for id_athl, heigth_athl in id_athls.items():
        
        if heigth_athl is None:
            continue
        
        nearest_abs = abs(user_heigth - heigth_athl)
        if not nearest or nearest_abs < nearest:
            nearest =nearest_abs
            athl_id = id_athl
            athl_heigth = heigth_athl

    return athl_id, athl_heigth

def str_to_date(date_str):

    date_test = date_str.replace("-", " ")
    datetime_object = datetime.strptime(date_test, "%Y %m %d")
   
    return datetime_object.date()

def main():

    session = connect_db()
    
    user_id = request_data()
    user = session.query(User).filter(User.id == user_id).first()

    if not user:
        print("Пользователь не найден в базе данных")
    else:
        athl_id_birthday, athl_birthday = find_bd(user, session)
        print("Ближайший атлет по дате рождения: {} родился: {}".format(athl_id_birthday, athl_birthday))
        athl_id_height, athl_heigth = find_height(user, session)
        print("Ближайший атлет по весу: {} родился: {}".format(athl_id_height, athl_heigth))

if __name__ == "__main__":
    main()