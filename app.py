from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config.DebugConfig)

@app.route('/')
def default():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()