#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from flask import Blueprint

public_pb = Blueprint('public', __name__)


@public_pb.route('/')
def index():
    return 'It works.'
