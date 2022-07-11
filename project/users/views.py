import random
# import logging

import requests
from celery.result import AsyncResult
from flask import render_template, request, jsonify

from . import users_blueprint
from project.users.forms import UserForm
from project.users.tasks import sample_task


def api_call(email):
    # used for testing a failed api call
    if random.choice([0, 1]):
        raise Exception('random processing error')

    # used for simulating a call to a third-party api
    requests.post('https://httpbin.org/delay/5')

@users_blueprint.route('/task_status/', methods=('GET', 'POST'))
def task_status():
    task_id = request.args.get('task_id')

    if task_id:
        task = AsyncResult(task_id)
        if task.state == 'FAILURE':
            error = str(task.result)
            response = {
                'state': task.state,
                'error': error,
            }
        else:
            response = {
                'state': task.state,
            }
        return jsonify(response)

# Used to test WebSocket transport
@users_blueprint.route('/form/', methods=('GET', 'POST'))
def subscribe_ws():
    form = UserForm()
    if form.validate_on_submit():
        task = sample_task.delay(form.email.data)
        return jsonify({
            'task_id': task.task_id,
        })
    return render_template('form.html', form=form)