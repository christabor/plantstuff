"""The front-end application for interacting with plant data.

Tools:

- view plants
- companion planter
- schedule maker
- analysis tools
"""

from flask import Flask, jsonify, render_template, request

from plantstuff.app import forms
from plantstuff.schema.plant import Plant


app = Flask(__name__)
app.config['SECRET_KEY'] = 'plantstuff'


@app.route('/', methods=['GET', 'POST'])
def index():
    """Homepage."""
    form = forms.make_form(Plant)
    kwargs = dict(form=form(request.args))
    return render_template('pages/index.html', **kwargs)


if __name__ == '__main__':
    app.run(debug=True)
