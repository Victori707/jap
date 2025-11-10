import os
from flask import Flask, send_from_directory, request, jsonify
from werkzeug.utils import secure_filename
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
DATA_FILE = os.path.join(BASE_DIR, 'data', 'itinerary.json')
UPLOAD_DIR = os.path.join(STATIC_DIR, 'photos')
ALLOWED_EXT = {'png','jpg','jpeg','webp'}
app = Flask(__name__, static_folder=STATIC_DIR, static_url_path='/static')

# serve index.html, js, css
@app.route('/')
def root():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/<path:p>')
def static_proxy(p):
    if os.path.exists(os.path.join(BASE_DIR, p)):
        return send_from_directory(BASE_DIR, p)
    elif os.path.exists(os.path.join(STATIC_DIR, p)):
        return send_from_directory(STATIC_DIR, p)
    return 'Not found', 404

@app.route('/data/itinerary.json', methods=['GET'])
def get_json():
    with open(DATA_FILE,'r',encoding='utf8') as f:
        return f.read(), 200, {'Content-Type':'application/json'}

@app.route('/data/itinerary.json', methods=['POST'])
def post_json():
    data = request.json
    if not data:
        return jsonify({'error':'empty'}),400
    with open(DATA_FILE,'w',encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return jsonify({'ok':True})

@app.route('/upload_photo', methods=['POST'])
def upload_photo():
    if 'photo' not in request.files:
        return jsonify({'error':'no file'}), 400
    file = request.files['photo']
    if file.filename == '':
        return jsonify({'error':'empty filename'}), 400
    ext = file.filename.rsplit('.',1)[-1].lower()
    if ext not in ALLOWED_EXT:
        return jsonify({'error':'bad ext'}), 400
    fname = secure_filename(file.filename)
    if not os.path.exists(UPLOAD_DIR): os.makedirs(UPLOAD_DIR)
    save_path = os.path.join(UPLOAD_DIR, fname)
    file.save(save_path)
    url = f'/static/photos/{fname}'
    return jsonify({'url':url})

@app.route('/save_html', methods=['POST'])
def save_html():
    html_content = request.form.get('html')
    if not html_content:
        return jsonify({'error':'no html content'}), 400
    html_file = os.path.join(BASE_DIR, 'index_saved.html')
    try:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        return jsonify({'ok':True, 'filename':'index_saved.html'})
    except Exception as e:
        return jsonify({'error':str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

