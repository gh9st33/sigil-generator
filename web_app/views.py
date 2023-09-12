```python
from flask import render_template, request, jsonify
from web_app import app
from web_app.models import Sigil
from web_app.utils import generate_sigil_code, save_image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_sigil():
    message = request.json['message']
    sigil_code = generate_sigil_code(message)
    sigil_image = save_image(sigil_code)
    sigil = Sigil(message=message, sigil_code=sigil_code, sigil_image=sigil_image)
    sigil.save()
    return jsonify({'sigilData': sigil.to_dict()})

@app.route('/sigil/<int:sigil_id>')
def get_sigil(sigil_id):
    sigil = Sigil.query.get_or_404(sigil_id)
    return render_template('sigil.html', sigilData=sigil.to_dict())
```