import asyncio

from db import Base, engine
from user import grpc_service
from config import USER_GRPC_SERVER_ADDR


if __name__ == "__main__":
    print("Start user gRPC server")
    Base.metadata.create_all(bind=engine)
    asyncio.run(grpc_service.start(USER_GRPC_SERVER_ADDR))
