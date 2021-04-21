#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bottle import request, get, post, static_file, route, run, template
import pyodbc as dbi
from itoolkit import *
from itoolkit.db2.idb2call import *     #for local jobs

@route('/sample')
def sample():
    return static_file('sample.html', root='.') 

@route('/query', method='POST')
def query_ibm_db():
    statement = request.forms.get('sql')

    conn = dbi.connect('DSN=DSN_Db2iBKP')
    cur = conn.cursor()
    cur.execute(statement)
    
    headers = [descr[0] for descr in cur.description]

    return template('query', headers=headers, rows=cur)


@route('/cmd', method='POST')
def cmd_toolkit():
    cl_statement = request.forms.get('cl')

    # xmlservice
    itool = iToolKit()
    itransport = iDB2Call()
    itool.add(iCmd5250(cl_statement, cl_statement))
    itool.call(itransport)
   
    # results from list   
    data = ''
    for output_outer in itool.list_out():
        for output_inner in output_outer:
            data += output_inner
    
    return template('cmd', data=data)

run(host='172.17.50.203', port=8000, debug=True, reloader=True)
