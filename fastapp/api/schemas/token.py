#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pydantic.main import BaseModel

"""
TODO token 模型，暂未启用

@File    :   token.py
@Time    :   2021/04/22 11:06:16
@Author  :   snc 
"""


class Token(BaseModel):
    type: str = "bearer"
    access_token: str