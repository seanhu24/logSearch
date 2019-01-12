from front import app
from flask import render_template

from utils.GetConfig import GetConfig


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    gc=GetConfig()
    sys_list=gc.get_paras()
    print(sys_list)
    return render_template('index.html', syslist=sys_list)

