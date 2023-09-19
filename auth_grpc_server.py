import asyncio

from db import Base, engine
from auth import grpc_servicer
from config import AUTH_GRPC_SERVER_ADDR


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    asyncio.run(grpc_servicer.start(AUTH_GRPC_SERVER_ADDR))
