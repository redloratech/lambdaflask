from flask import Flask
import pandas as pd
from sqlalchemy import create_engine
import json
app = Flask(__name__)

@app.route('/get5ticker')
def get_5ticker():
    engine = create_engine("postgres://postgres:askLORA20$@droid-test.cgqhw7rofrpo.ap-northeast-2.rds.amazonaws.com:5432/postgres")
    data = pd.read_sql("SELECT ticker, count(event)FROM classic_backtest WHERE event='TP' GROUP BY ticker,event ORDER BY COUNT(event) DESC LIMIT 5", con=engine)
    data = data.to_json(orient='records')

    return data

# We only need this for local development.
if __name__ == '__main__':
 app.run()