from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)  # ✅ betul: __name__

@app.route('/')
def upload_form():
    return '''
        <h2>Upload File CSV</h2>
        <form action="/analyze" method="post" enctype="multipart/form-data">
            <input type="file" name="file" accept=".csv" required>
            <button type="submit">Proses</button>
        </form>
    '''

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    if not file:
        return 'No file uploaded.', 400
    df = pd.read_csv(file)
    stats = df.describe().T[['mean', '50%', 'std']]
    stats.rename(columns={'50%': 'median'}, inplace=True)
    return stats.to_html(classes='table table-striped')

if __name__ == '__main__':  # ✅ betul: __main__
    app.run(host='0.0.0.0', port=5000)
