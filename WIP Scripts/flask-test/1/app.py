from flask import Flask, render_template, request, jsonify
import languagemodels as lm
import time

app = Flask(__name__)

lm.set_max_ram('2gb')
zone = time.tzname[0]

if(time.localtime().tm_isdst == 1):
    daylightsavings = "Daylight Savings is in effect."
else:
    daylightsavings = "Daylight Savings is not in effect."

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/generate-response', methods=['POST'])
def chat():
    message = request.form['text-input']
    response = lm.chat(f'''
        System: The assistant gives helpful, detailed, and polite answers to the human's questions. Limited to only one interaction, resulting in no memory of any previous interactions. It is currently {lm.get_date()} {zone}.{daylightsavings} 
        User: {message}
        Assistant:
    ''')
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)