import os 

from dotenv import load_dotenv


load_dotenv()

SQLALCHEMY_DATABASE_URL = str(os.getenv("DATABASE_URL"))

JWT_SECRET_KEY = str(os.getenv("JWT_SECRET_KEY"))
JWT_REFRESH_SECRET_KEY = str(os.getenv("JWT_REFRESH_SECRET_KEY"))
