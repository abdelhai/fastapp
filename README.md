# A simple API with FastAPI and Deta

Do not clone the repo if you are learning, just follow along.

## Make sure you have a Deta account

[Make an account](https://web.deta.sh/) and confirm it, it's free.


## Install the Deta CLI and make sure you're logged in

[Follow these instruction](https://docs.deta.sh/docs/cli/install) to get the Deta CLI up and running.

## Create a project directory and files

To create a directory, in the terminal, run the following:

```
mkdir fastapp
```

Then change into the directory:

```
cd fastapp
```

and make two empty files:

```
touch main.py requirements.txt
```

## Add FastAPI to your dependancies

In the `requirements.txt` file add `fastapi`:

```
fastapi
```

## Import FastAPI and write your first endpoint

In `main.py`, add the following code:

```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return "Hello from Deta!"
```

## Deploy you code to Deta and test

To deploy to Deta, run the following command inside the project directory, aka `fastapp`:

```
deta new
```

The deployment should take a few seconds. Make sure to notice the Micro URL, it will look somethign like this:

```
https://xyz.deta.dev/
```

You can open it in your browser and it if everything has worked, then you will see:

```
Hello from Deta!
```

## Deploy changes

You can deploy changes to Deta using this command:

```
deta deploy
```

You could also use the convenient `watch` command for auto-deploys

## See the logs and debug your API using VISOR

To open VISOR, run the following:

```
deta visor open
```

## Protect your API

To protect your API, so no one else but you could access it, run the following:

```
deta auth enable
```

You can re-open you API by running:

```
deta auth disable
```

To create an API key, run the following command

```
deta auth create-api-key --name name-of-the-key 
```

Make sure to keep it in a secure place.


## Resources

- [Deta Docs](https://docs.deta.sh/docs/home) / [Deta Base](https://docs.deta.sh/docs/base/about)
- [FastAPI Docs](https://fastapi.tiangolo.com/) / [Official tutorial](https://fastapi.tiangolo.com/deployment/deta/)
- [Awesome Deta](https://github.com/deta/awesome-deta)

