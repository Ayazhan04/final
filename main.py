from website import create_app
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request

app = create_app()

if __name__ == '__main__':
  app.run(debug=True)