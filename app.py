from flask import Flask, request, jsonify
import joblib


app = Flask(__name__)
model = joblib.load('./model_rf')


def cal_volume(model, vol_moving_avg, adj_close_rolling_med):
    result = model.predict( [[vol_moving_avg, adj_close_rolling_med]])
    return int(result[0])

def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False    

def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False 
    
  
@app.route('/predict')
def get_volume():
    vol_moving_avg = request.args.get('vol_moving_avg')
    adj_close_rolling_med = request.args.get('adj_close_rolling_med')
    
    if not vol_moving_avg or not adj_close_rolling_med:
        return jsonify({'error': 'You need to supply a text'}), 400
    elif not is_int(vol_moving_avg) and not is_float(vol_moving_avg):
         return jsonify({'error': 'vol_moving_avg and adj_close_rolling_med should be of int/float type'}), 400 
    elif not is_int(adj_close_rolling_med) and not is_float(adj_close_rolling_med) :
          return jsonify({'error': 'vol_moving_avg and adj_close_rolling_med should be of int/float type'}), 400    

    return jsonify({'volume': cal_volume(model, vol_moving_avg, adj_close_rolling_med)}), 200



@app.route('/hello')
def hello_world():
    print("yes=======================")
    return 'Hello, World!wow!!!!!!!!!!!!!!!!!!!!!'

if __name__ == "__main__":
    app.run(port=8000, debug=True)









