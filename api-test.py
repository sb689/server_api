import requests

def test1():
    url = 'http://localhost:8000/predict_volume?vol_moving_avg=20650&adj_close_rolling_med=0.97'
    res = requests.get(url)
    print("all positive test status_code: %d, response: %s" % (res.status_code, res.text))


def test2():
    url = 'http://localhost:8000/predict_volume?vol_moving_avg=ab&adj_close_rolling_med=0.97'
    res = requests.get(url)
    print("vol_moving_avg string test status_code: %d, response: %s" % (res.status_code, res.text))


def test3():
    url = 'http://localhost:8000/predict_volume?vol_moving_avg=20650&adj_close_rolling_med=ab'
    res = requests.get(url)
    print("adj_close_rolling_med string test status_code: %d, response: %s" % (res.status_code, res.text))


test1()
test2()  
test3()  