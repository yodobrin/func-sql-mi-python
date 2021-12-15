import logging
import datetime
import datetime as dt
import io
import itertools
import json
import logging
import math
import os
import pickle
import sqlite3
import time
from collections import OrderedDict
from contextlib import redirect_stdout
from datetime import date, datetime, timedelta
from decimal import *
from functools import reduce
from itertools import chain
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd
import pyodbc
import requests
from dateutil.relativedelta import relativedelta
from pandas.tseries.offsets import MonthEnd
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # query = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')
  
    conn_str = os.environ['my_sql_cs']
    print(conn_str)
    cnxn = pyodbc.connect(conn_str)
    cursor = cnxn.cursor()
    query = "select *  from sys.tables"
    query2 = "select * from [dbo].[address]"
    
    a = np.array([1, 2, 3, 4, 5, 6])

    cursor.execute(query2)
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    
 
    return func.HttpResponse(f"results: {results}")    


