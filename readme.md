# Basic Events

Simple Event App in Django.

# Status

This is just started :)


# Install

```
pip install -r requirements/development.txt
./manage.py migrate

./manage.py runserver
or
./manage.py runserver_plus
```

## Docker
To build a fresh image from the Dockerfile:

```
docker build .
```

See whats running
```
docker ps
```

## Testing
This doesnt make FK relationships or PK's, dont use it.

```
./manage.py seed events --number=40
```


This runs the Unit Tester Suite
```
$ py.test
```

## Test Coverage
This triggers `Makefile` which triggers `bin/coverage.sh`
```
make test
```


