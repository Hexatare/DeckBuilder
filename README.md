# DeckBuilder

## How to write code

- Type hinting: "x: int = 0" instead of just "x = 0"
- Pylint: Install pylint using "pip install pylint"

## Build Docker Container
`docker build --tag deck-builder .`
`docker run -p 5000:5000 --env-file .env deck-builder`


## Gunicorn
Important! Gunicorn runs the app on port 8000 instead of 5000. If port 5000 is configured for the server name in the .env file, this needs to be changed or a 404 page will be shown for every page.