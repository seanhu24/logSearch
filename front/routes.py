from front import app
from flask import render_template, flash, redirect, url_for, send_file
from front.forms import LoginForm, SearchForm, DownloadForm
from utils.GetConfig import GetConfig
from app.SearchFile import SearchFile


@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    form = SearchForm()
    if form.validate_on_submit():

        dir_location = form.server.data
        file_pattern = form.file_pattern.data
        keyword = form.keyword.data
        flash('查询路径:{},文件模式:{},查询条件:{}'.format(
            dir_location, file_pattern, keyword))

        sf = SearchFile(dir_location)
        if file_pattern == '':
            files = sf.get_all_files()
        else:
            files = sf.get_all_files(file_pattern)

        grep_results = []
        for file in files:
            grep_results.extend(sf.grep_file(file, keyword, 0))

        return render_template('search_result.html', form=form,
                               dir_location=dir_location, file_pattern=file_pattern, keyword=keyword, grep_results=grep_results)
    return render_template('index.html', form=form)


@app.route('/download', methods=['POST', 'GET'])
def download():
    form = DownloadForm()
    if form.validate_on_submit():
        flash('下载文件:{}'.format(form.filename.data))
        # print("$$$"+form.filename.data)
        try:
            return send_file(form.filename.data, as_attachment=True)
        except FileNotFoundError:
            return render_template('download.html', form=form, errormsg='找不到文件')

    return render_template('download.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
