from flask import Flask, request, jsonify

from clustering.classify import classify, correlation_coef

app = Flask(__name__)


@app.route('/clusterization', methods=['POST'])
def clusterization():
    if request.method == 'POST':
        data = request.json
        if data.get('question', None):
            result = classify(data['question'], True, 0)
            result_dict = dict()
            result_dict['disciplines'] = [{item[0]: f'{round(item[1] * 100, 2)}'} for item in result] if result else [{'Other': 100}, ]
            result_dict['correlation'] = dict()
            result_dict['correlation']['value'] = round(correlation_coef(result[0][0], result[1][0]), 4)
            result_dict['correlation']['description'] = f'Correlation coefficient between "{result[0][0]}" and "{result[1][0]}"'

            return jsonify(result_dict), 200
        else:
            return jsonify(
                dict(errors='question field is not valid')
            )


if __name__ == '__main__':
    app.run(debug=True)