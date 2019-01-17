## 环境变量设置
* in windows: 
> set FLASK_APP=run.py
> set FLASK_ENV=development
* in linux: 
> export FLASK_APP=run.py
> export FLASK_ENV=development

## 目录配置文件
config.py

## 短信平台IP地址
```
/etc/hosts中配置
SMS_SERVER
```

## 安装包
'''
Flask-WTF==0.14.2
  - Flask [required: Any, installed: 1.0.2]
    - click [required: >=5.1, installed: 7.0]
    - itsdangerous [required: >=0.24, installed: 1.1.0]
    - Jinja2 [required: >=2.10, installed: 2.10]
      - MarkupSafe [required: >=0.23, installed: 1.1.0]
    - Werkzeug [required: >=0.14, installed: 0.14.1]
  - WTForms [required: Any, installed: 2.2.1]
'''
