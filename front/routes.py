from front import app
from flask import render_template, flash, redirect, url_for, send_file
from front.forms import LoginForm, SearchForm, DownloadForm
from utils.GetConfig import GetConfig
from app.SearchFile import SearchFile
import json
import os
import re


@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    form = SearchForm()
    try:
        if form.validate_on_submit():

            dir_locations = json.loads(form.server.data)
            # print(type(dir_locations))
            # print("$$", dir_locations)
            file_pattern = form.file_pattern.data
            keyword = form.keyword.data

            file_pattern_split = os.path.split(file_pattern)

            file_pattern = file_pattern_split[1]

            flash('查询路径:{},文件模式:{},查询条件:{}'.format(
                dir_locations, file_pattern, keyword))

            files = []
            for dir_location in dir_locations:
                # print('$', dir_location)
                sf = SearchFile(os.path.join(
                    dir_location, file_pattern_split[0]))
                if file_pattern == '':
                    files.extend(sf.get_all_files())
                else:
                    print(file_pattern)
                    files.extend(sf.get_all_files(file_pattern))
            # print(files)
            grep_results = []
            for file in files:
                grep_results.extend(sf.grep_file(file, keyword, 0))

            format_res = []
            for res in grep_results:
                for k, v in res.items():

                    path = '?'.join(os.path.normpath(k).split(os.sep))

                    k2 = '<a href=' + \
                        url_for('download_a_file', fname=path) + \
                        '>' + k + '</a>'
                format_res.append({k2: v})
            return render_template('search_result.html', form=form,
                                   dir_location=dir_locations, file_pattern=file_pattern, keyword=keyword, grep_results=format_res)
    except Exception as e:
        print(e)
    return render_template('index.html', form=form)


@app.route('/download_a_file/<fname>', methods=['POST', 'GET'])
def download_a_file(fname):
    # print('downloading file', fname)
    fname = re.sub('\?', '/', fname)
    print('downloading file', fname)
    flash('下载文件:{}'.format(fname))
    try:
        return send_file(fname, as_attachment=True)
    except FileNotFoundError:
        render_template('download.html', errormsg='找不到文件')


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
