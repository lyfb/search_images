#!/usr/bin/env python
# @Time    : 2020/5/11 16:51
# @Author  : 洪英杰
# @Python  : 3.7.5
# @File    : migrate
# @Project : search_images
from config import model_name
from store import Store


if __name__ == '__main__':
    db = Store(index=model_name, model_name=model_name)
    # db.delete_index()
    db.create_index()
    db.save_feature()
