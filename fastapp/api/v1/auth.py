#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from authlib.integrations.starlette_client import OAuth
from fastapi import APIRouter, Request

from fastapp.core.config import settings

"""
# 描述

@File    :   auth.py
@Time    :   2021/04/19 15:31:44
@Author  :   snc 
"""

router = APIRouter()

oauth = OAuth()

oauth.register(
    name='github',
    client_id=settings.OAUTH2_GITHUB.CLIENT_IDs,
    client_secret=settings.OAUTH2_GITHUB.CLIENT_SECRET,
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)


@router.get("/login/github")
async def login_via_github(request: Request):
    redirect_uri = request.url_for('auth_via_github')
    return await oauth.github.authorize_redirect(request, redirect_uri)


@router.get("/auth/github")
async def auth_via_github(request: Request):
    token = await oauth.github.authorize_access_token(request)
    resp = await oauth.github.get('user', token=token)
    user = resp.json()
    email = await oauth.github.get('user/emails', token=token)
    return user
