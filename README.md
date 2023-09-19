# DeckBuilder

## How to write code
- Type hinting: "x: int = 0" instead of just "x = 0"
- Pylint: Install pylint using "pip install pylint"

## Build Docker Container
`docker build --tag deck-builder .`
`docker run -p 5000:5000 --env-file .env deck-builder`
