import asyncio

from db import Base, engine
from user import grpc_servicer
from config import USER_GRPC_SERVER_ADDR


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    asyncio.run(grpc_servicer.start(USER_GRPC_SERVER_ADDR))
