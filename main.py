# -*- coding: utf-8 -*-

import logging
from flask import Flask, request, redirect
from google.appengine.ext import ndb


app = Flask(__name__)

class Namespace(ndb.Model):
    namespace = ndb.StringProperty()
    count = ndb.IntegerProperty()

class Item(ndb.Model):
    number = ndb.IntegerProperty()


@app.route('/')
def handler_root():
    return redirect("https://github.com/paulo-raca/count-things")

@app.route('/<path:namespaces>/')
def handler_nokey(namespaces):
    return get_count(namespaces.split('/'))

@app.route('/<path:namespaces>/<key>')
def handler_withkey(namespaces, key):
    return get_count(namespaces.split('/'), key)

def pretty_key(key):
    return u'»'.join(key.flat()[1::2])

@ndb.transactional
def get_count(namespaces, item=None):
    fmt = request.args.get('format', '%d')
    namespace_key=None
    namespace_obj=None
    
    for namespace in namespaces:
        namespace_key = ndb.Key(Namespace, namespace, parent=namespace_key)
        namespace_obj = namespace_key.get()
        if namespace_obj is None:
            namespace_obj = Namespace(key=namespace_key, count=0)
            namespace_obj.put()
            logging.info('Created namespace %s', pretty_key(namespace_key))
    
    if item is None:
        namespace_obj.count += 1
        namespace_obj.put()
        logging.info('Counting unnamed item on namespace %s = %d', pretty_key(namespace_key), namespace_obj.count)
        return fmt.format(namespace_obj.count)
    else:
        item_key = ndb.Key(Item, item, parent=namespace_key)
        item_obj = item_key.get()
        if item_obj is None:
            namespace_obj.count += 1
            namespace_obj.put()
            item_obj = Item(key=item_key, number=namespace_obj.count)
            item_obj.put()
            logging.info('Created item %s = %d', pretty_key(item_key), item_obj.number)
        else:
            logging.info('Existing item %s = %d', pretty_key(item_key), item_obj.number)
        return fmt.format(namespace_obj.count)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

