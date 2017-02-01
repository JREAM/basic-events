# Basic Events

Simple Event App in Django.

# Status

This is just started :)

# Install

```
pip install -r requirements/development.txt
./manage.py migrate
./manage.py seed events --number=40


./manage.py runserver
or
./manage.py runserver_plus
```

## Testing
This runs the Unit Tester Suite
```
$ py.test
```

## Test Coverage
This triggers `Makefile` which triggers `bin/coverage.sh`
```
make test
```


