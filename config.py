import os

from dotenv import load_dotenv


load_dotenv()

SQLALCHEMY_DATABASE_URL = str(os.getenv("DATABASE_URL"))

JWT_SECRET_KEY = str(os.getenv("JWT_SECRET_KEY"))
JWT_REFRESH_SECRET_KEY = str(os.getenv("JWT_REFRESH_SECRET_KEY"))

BLOG_GRPC_SERVER_ADDR = "0.0.0.0:50051"
AUTH_GRPC_SERVER_ADDR = "0.0.0.0:50052"
USER_GRPC_SERVER_ADDR = "0.0.0.0:50053"
