from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/members", methods=['GET','POST'])
def get_members():
    try:
        # Stock Symbol을 받아옴
        data = request.get_json()
        stock_symbol = data.get('stocksymbol', '')
        print(stock_symbol)
        
        # Stock Symbol에 '!' 추가
        modified_data = [{'id': i + 1, 'value': f'{stock_symbol}!'} for i in range(len(stock_symbol))]

        # JSON 형식으로 반환
        return jsonify(modified_data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
