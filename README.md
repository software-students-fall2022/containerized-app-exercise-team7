[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9335331&assignment_repo_type=AssignmentRepo)

# Containerized App Exercise

Build a containerized app that uses machine learning. See [instructions](./instructions.md) for details.

[1, Local mongodb setup within Docker](#local-mongodb-database-set-up-within-docker)

[2, Root environment](#root-environment)

[3, Required dependencies](#required-dependencies)

## Local mongodb database set up within Docker

### 1, Docker Desktop

Make sure Docker Desktop is installed, if not check [here](https://www.docker.com/products/docker-desktop/).

### 2, Mongo image

Pull the mongo image by running the following command in terminal

```bash
docker pull mongo
```

### 3, Run container

Once installed, run the mongo container with the following command:

```bash
docker run -itd --name mongo -p 27017:27017 mongo --auth
```

### 4, Set up admin

We can either connect to to mongo by opening the terminal inside Docker Desktop or run the following command in terminal:

```bash
docker exec -it mongo mongo admin
```

**If using the terminal inside Docker Desktop, use mongosh to get connection:**

```bash
# mongosh
```

Create a user named admin with a password of 123456:

```bash
db.createUser({ user:'admin',pwd:'123456',roles:[ { role:'userAdminAnyDatabase', db: 'admin'},"readWriteAnyDatabase"]});
```

Try to connect using the user information created above.

```bash
db.auth('admin', '123456')
```

## Root environment

Create a `.env` file and can set them as environment variables.

Under root for the project, create `.env` file with content:

```env
FLASK_ENV = development

MONGO_URI = mongodb://localhost:27017/
MONGO_DBNAME = language
```

## Required dependencies

```python
pip install deep_translator
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio
pip install flask
pip install pymongo
```
## Supported Languages
English
Chinese
French
Spanish
Japanese
## Contributors

[Darren Le](https://github.com/DarrenLe20)

[Daniel Atlas](https://github.com/Spectraorder)

[Paula Seraphim](https://github.com/paulasera)

[Leo Xu](https://github.com/leo6016)

[Hillary Davis](https://github.com/hillarydavis1)

[Kedan Zha](https://github.com/Zackdan0227)
