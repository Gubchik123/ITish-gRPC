import asyncio

from db import Base, engine
from grpc_services import auth
from config import AUTH_GRPC_SERVER_ADDR


if __name__ == "__main__":
    print("Start auth gRPC server")
    Base.metadata.create_all(bind=engine)
    asyncio.run(auth.start(AUTH_GRPC_SERVER_ADDR))
