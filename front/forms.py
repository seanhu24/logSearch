from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired
from utils.GetConfig import GetConfig


class LoginForm(FlaskForm):
    username = StringField('用户', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登陆')


class SearchForm(FlaskForm):
    gc = GetConfig()
    choices = []
    choices.extend([(v, k) for k, v in gc.get_paras().items()])
    # print(choices)
    server = SelectField('选择系统', choices=choices)
    file_pattern = StringField('文件模式')
    keyword = StringField('关键字', validators=[DataRequired()])
    submit = SubmitField('提交')


class DownloadForm(FlaskForm):
    filename = StringField('文件绝对路径', validators=[DataRequired()])
    submit = SubmitField('下载')


if __name__ == "__main__":
    gc = GetConfig()
    print(gc.get_params())
