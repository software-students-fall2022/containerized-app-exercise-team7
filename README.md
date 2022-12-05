[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9335331&assignment_repo_type=AssignmentRepo)

![Workflow Status](https://github.com/software-students-fall2022/containerized-app-exercise-team7/actions/workflows/webapp_test.yml/badge.svg?event=push)

![Workflow Status](https://github.com/software-students-fall2022/containerized-app-exercise-team7/actions/workflows/machine_learning_test.yml/badge.svg?event=push)

# Containerized App Exercise

Build a containerized app that uses machine learning. See [instructions](./instructions.md) for details.

[1, Local mongodb setup within Docker](#local-mongodb-database-set-up-within-docker)

[2, Root environment](#root-environment)

[3, Required dependencies](#required-dependencies)

[4, Usage Instructions](#usage-instructions)

[5, Supported Languages](#supported-languages)

[6, Contributors](#contributors)

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

Then in order to set up an admin account:

```bash
# use admin
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
FLASK_DEBUG = development

MONGO_URI = mongodb://localhost:27017/
MONGO_DBNAME = language
MONGO_USER = admin
MONGO_PASS = 123456
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

## Usage Instructions

RECORD a voice message in English

- Pause button: Temporary stop recording

- Stop button: Stop recording

UPLOAD or SAVE the voice message

- Upload button: Upload the voice message to the database

- Save button: Save the voice message to the local machine

CHOOSE a language to translate the recording to

- Select a language from the dropdown menu

TRANSLATE the recording by clicking the translate button

## Supported Languages

### Input language

- English

### Output languages

- Bulgarian
- Czech
- Danish
- German
- Greek
- English
- Spanish
- Estonian
- Finnish
- French
- Hungarian
- Italian
- Japanese
- Lithuania
- Latvian
- Dutch
- Polish
- Portuguese
- Romanian
- Russian
- Slovak
- Swedish
- Turkish
- Ukrainian
- Chinese

## Contributors

[Darren Le](https://github.com/DarrenLe20)

[Daniel Atlas](https://github.com/Spectraorder)

[Paula Seraphim](https://github.com/paulasera)

[Leo Xu](https://github.com/leo6016)

[Hillary Davis](https://github.com/hillarydavis1)

[Kedan Zha](https://github.com/Zackdan0227)
