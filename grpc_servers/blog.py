import asyncio

from db import Base, engine
from grpc_services import blog
from config import BLOG_GRPC_SERVER_ADDR


if __name__ == "__main__":
    print("Start Blog gRPC server")
    Base.metadata.create_all(bind=engine)
    asyncio.run(blog.start(BLOG_GRPC_SERVER_ADDR))
