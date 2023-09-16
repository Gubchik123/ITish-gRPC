import asyncio

from db import Base, engine
from blog import grpc_service
from config import BLOG_GRPC_SERVER_ADDR


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    asyncio.run(grpc_service.start(BLOG_GRPC_SERVER_ADDR))
