# Django sample with docker

This is a sample Django project running on Docker. 

## Setting up & running the app

Simply run `./scripts/up.sh`. That will create the django images if they don't
exist, set them up and run them. If you want to run it in detached mode,
you can run `./scripts/dup.sh`. For more information about the docker-compose
up, check the [docker documentation](https://docs.docker.com/compose/reference/up/).

## Running migrations and other manage commands

I've created a script for that: `./scripts/managepy.sh`. Some examples:

- `./scripts/managepy.sh migrate`
- `./scripts/managepy.sh createsuperuser`

That command will run the application in the foreground. If you want to run
it as a daemon, run `./scripts/dup.sh`.

## Stopping the app

Run `./scripts/stop.sh` for stopping the app or `./scripts/down.sh` for stopping it
and taking down images, containers, networks, etc. For more information about
these commands:

- [docker-compose down](https://docs.docker.com/compose/reference/down/)
- [docker-compose stop](https://docs.docker.com/compose/reference/stop/)

## Working with PyCharm

PyCharm allows setting up a remote python interpreter and also integrates
well with Docker, so setting it up to use the Docker image python interpreter
should be easy. For more information, take a look at
[this help page](https://www.jetbrains.com/help/pycharm/docker-using-docker-as-a-remote-interpreter.html).

If you are using an editor that doesn't support remote interpreters, I'd suggest
creating a virtualenv and installing the requirements.txt dependencies to get
autocomplete / code suggestions.
