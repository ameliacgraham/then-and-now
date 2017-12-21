from flask import Flask, jsonify, render_template, redirect, request
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key= "NKASLNVDNLJDSK"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def display_homepage():
    "Displays the homepage."

    return "Hello World"

if __name__ == "__main__":

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode
    # if app.config['TESTING'] is True:
    #     connect_to_db(app, "postgresql:///testdb")
    # else:
    #     connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)
    
    app.run(port=5000, host='0.0.0.0')