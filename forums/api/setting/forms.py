#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: forms.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-20 22:13:24 (CST)
# Last Update:星期三 2016-12-21 22:2:46 (CST)
#          By:
# Description:
# **************************************************************************
from flask_wtf import Form
from flask_babelex import lazy_gettext as _
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import Length, DataRequired, EqualTo
from flask_wtf.file import FileField, FileAllowed, FileRequired
from api.user.models import UserSetting
from flask import redirect, url_for

choices = UserSetting.STATUS
timezone = UserSetting.TIMEZONE
locale = UserSetting.LOCALE


def error_callback(url):
    return lambda: redirect(url_for(url))


class AvatarForm(Form):
    avatar = FileField(
        _('Upload Avatar:'),
        validators=[FileRequired(), FileAllowed(['jpg', 'png'],
                                                '上传文件只能为图片且图片格式为jpg,png')])

class PrivacyForm(Form):
    online_status = SelectField(
        _('Login status:'), coerce=str, choices=choices)
    topic_list = SelectField(_('Topic List:'), coerce=str, choices=choices)

    rep_list = SelectField(_('Reply List:'), coerce=str, choices=choices)
    ntb_list = SelectField(_('Notebook List:'), coerce=str, choices=choices)
    collect_list = SelectField(_('Collect List:'), coerce=str, choices=choices)


class ProfileForm(Form):
    introduce = TextAreaField(_('Introduce:'), [Length(max=256)])
    school = StringField(_('School:'), [Length(max=256)])
    word = TextAreaField(_('Signature:'), [Length(max=256)])


class PasswordForm(Form):
    old_password = PasswordField(
        _('Old Password:'), [DataRequired(), Length(
            min=4, max=20)])
    new_password = PasswordField(
        _('New Password:'), [DataRequired(), Length(
            min=4, max=20)])
    rnew_password = PasswordField(
        _('New Password again:'), [DataRequired(), EqualTo('new_password')])


class BabelForm(Form):
    timezone = SelectField(_('Timezone:'), coerce=str, choices=timezone)
    locale = SelectField(_('Locale:'), coerce=str, choices=locale)
