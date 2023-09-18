#!/usr/bin/env python
"""This is the main script to run the flask app"""


# Imports
from deck_builder import init_app


# Call the init_app function
app = init_app()


# Entry point
if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
