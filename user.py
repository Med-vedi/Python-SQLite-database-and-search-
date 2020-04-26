import sqlalchemy as sa 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import sys

DB_PATH = 'sqlite:///'+sys.argv[1]
Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	id = sa.Column(sa.INTEGER, primary_key=True)
	first_name = sa.Column(sa.TEXT)
	last_name = sa.Column(sa.TEXT)
	gender = sa.Column(sa.TEXT)
	email = sa.Column(sa.TEXT)
	birthdate = sa.Column(sa.TEXT)
	height = sa.Column(sa.FLOAT)

def connect_db():
	engine = sa.create_engine(DB_PATH)
	Base.metadata.create_all(engine)
	session = sessionmaker(engine)

	return session()

def request_data():
	print('Привет! Я сохраню твои данные (а потом продам спаммерам ;)')

	first_name = input('Как зовут? :')
	last_name = input('А фамилия? :')
	gender = input('М или Ж: вводить Male или Female...')
	birthdate = input('Дата рождения: (yyyy-mm-dd)...')

	email = input('Давай и почтовый ящик (пиши шо хошь, валидатора по ТЗ нет))) : ')
	height = input('Рост: (m.cm)...')
	user = User(
		# id=user_id
		first_name= first_name,
		last_name=last_name,
		gender=gender,
		email=email,
		birthdate=birthdate,
		height=height)
	return user

def user_registration():
	session = connect_db()
	user = request_data()
	session.add(user)
	session.commit()
	print('Сохранил атлета:', user.first_name, user.last_name) 

def main():
	mode = input('Введи:\n1, чтобы получить 5$ и пройти регистрацию\n2, чтобы просто пройти регистрацию\n')

	if mode =='1':
		print('Да шучу я, давай регистрируйся...')
		user_registration()
	elif mode == '2':
		user_registration()
	else:
		print('Все фигня, давай по-новой')

if __name__ == '__main__':
	main()
