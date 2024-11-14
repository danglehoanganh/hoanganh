from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')
    # Bật chế độ debug
app.config["DEBUG"] = True



if __name__ == '__main__':
    app.run(debug=True)
