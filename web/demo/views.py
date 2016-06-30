import json
from flask import render_template, request, redirect, make_response
from web.demo import demo


@demo.route('/post', methods=['POST']) # TODO: move to client
def _post():
    if request.method == 'POST':
        data = request.form
        total = 0
        choices = []
        for key in data:
            if key.startswith('n') and data[key] and int(data[key]) > 0:
                choices.append((int(key.split('n')[1]), int(data[key])))
                total += int(data[key])
        resp = make_response(redirect('/siat'))
        resp.set_cookie('choices', json.dumps(choices))
        resp.set_cookie('total', json.dumps({'total':total}))
        return resp

@demo.route('/siat')
def _peit():
    choices = json.loads(request.cookies.get('choices'))
    total = json.loads(request.cookies.get('total'))
    return render_template('confirm.html', choices=choices, total=total)

@demo.route('/peit')
def _siat():
    rows = range(1,101)[::5]
    return render_template('choose.html', rows=rows)
