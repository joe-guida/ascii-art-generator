from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(Config.DefaultConfig)

@app.route('')
async def default():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run()