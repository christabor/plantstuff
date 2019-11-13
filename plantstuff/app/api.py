"""The back-end API application for interacting with plant data.

API [wip]

/plants {GET}
/plants/<id> {GET}
"""

from flask import Flask


app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)
