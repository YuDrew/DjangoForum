#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:34:29 2020

@author: yudrew
"""

from django.urls import path
from . import views

app_name = "forums"

urlpatterns = [
    path("", views.home, name = "home"),
    path("about/", views.about, name = "about"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("register/", views.register, name="register"),
    path("account/", views.account, name="account"),
]