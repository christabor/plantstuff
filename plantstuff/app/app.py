"""The front-end application for interacting with plant data.

Tools:

- view plants
- companion planter
- schedule maker
- analysis tools
"""
import inspect

from flask import Flask, abort, jsonify, render_template, request
from plantstuff.app import forms
from plantstuff.schema_graph import models
from plantstuff.schema_graph.models.plant import Plant

# from plantstuff.schema.plant import Plant


app = Flask(__name__)
app.config['SECRET_KEY'] = 'plantstuff'


def get_schemas():
    modules = inspect.getmembers(models, inspect.ismodule)
    all_schema_classes = [
        inspect.getmembers(module, inspect.isclass) for name, module in modules
    ]
    return all_schema_classes


@app.route('/schema/<name>', methods=['GET'])
def inspect_schema(name):
    """Homepage."""
    modules = inspect.getmembers(models, inspect.ismodule)
    relevant = [module for (item, module) in modules if item == name]
    if not relevant:
        abort(404, f'Module {name} not found')
    classes = inspect.getmembers(relevant[0], inspect.isclass)
    # Filter out imports.
    classes = [(name, klass) for (name, klass) in classes
               if 'schema_graph.models' in str(klass)]
    return render_template('pages/module.html', name=name, classes=classes)


@app.route('/', methods=['GET'])
@app.route('/schema', methods=['GET'])
def index():
    """Homepage."""
    modules = inspect.getmembers(models, inspect.ismodule)
    return render_template('pages/index.html', modules=modules)


@app.route('/search', methods=['GET'])
def search():
    """Homepage."""
    # form = forms.make_form(Plant)
    # kwargs = dict(form=form(request.args))
    all_schemas = get_schemas()
    return render_template('pages/search.html', all_schemas=all_schemas)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
