<img title="ITish gRPC" alt="Header image" src="./header.png">

_gRPC for my blog site [ITish](https://itish.live)_

## Purpose

My blog site [ITish](https://itish.live) ([GitHub](https://github.com/Gubchik123/ITish)) was written using templates, but in our time there are not a lot of projects that use templates. That's why here is gRPC of the "ITish"

## Project modules

<a href='https://pypi.org/project/grpcio'><img alt='grpcio' src='https://img.shields.io/pypi/v/grpcio?label=grpcio&color=blue'></a> <a href='https://pypi.org/project/grpcio-health-checking'><img alt='grpcio-health-checking' src='https://img.shields.io/pypi/v/grpcio-health-checking?label=grpcio-health-checking&color=blue'></a> <a href='https://pypi.org/project/grpcio-reflection'><img alt='grpcio-reflection' src='https://img.shields.io/pypi/v/grpcio-reflection?label=grpcio-reflection&color=blue'></a> <a href='https://pypi.org/project/grpcio-tools'><img alt='grpcio-tools' src='https://img.shields.io/pypi/v/grpcio-tools?label=grpcio-tools&color=blue'></a> <a href='https://pypi.org/project/bcrypt'><img alt='bcrypt' src='https://img.shields.io/pypi/v/bcrypt?label=bcrypt&color=blue'></a> <a href='https://pypi.org/project/passlib'><img alt='passlib' src='https://img.shields.io/pypi/v/passlib?label=passlib&color=blue'></a> <a href='https://pypi.org/project/python-dotenv'><img alt='python-dotenv' src='https://img.shields.io/pypi/v/python-dotenv?label=python-dotenv&color=blue'></a> <a href='https://pypi.org/project/python-jose'><img alt='python-jose' src='https://img.shields.io/pypi/v/python-jose?label=python-jose&color=blue'></a> <a href='https://pypi.org/project/SQLAlchemy'><img alt='SQLAlchemy' src='https://img.shields.io/pypi/v/SQLAlchemy?label=SQLAlchemy&color=blue'></a> 

> Look at the requirements.txt

## Environment Variables

To run this project, you will need to add the following environment variables:

`DATABASE_URL`
`JWT_SECRET_KEY` `JWT_REFRESH_SECRET_KEY`

> Look at the file_env_example.txt

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/Gubchik123/ITish-gRPC.git
    ```

2. Go to the project directory:

    ```
    cd ITish-gRPC
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

5. Run the gRPC servers:
    ```
    python blog_grpc_server.py
    python auth_grpc_server.py
    python user_grpc_server.py
    ```

    > **Note:** Don't forget about environment variables