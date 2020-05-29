#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:34:29 2020

@author: yudrew
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name = "forums-home"),
    path("about/", views.about, name = "forums-about"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("register/", views.register, name="register"),
]