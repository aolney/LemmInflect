from flask import Flask, request, jsonify
from lemminflect import getLemma, getAllLemmas, getAllLemmasOOV, isTagBaseForm
from lemminflect import getInflection, getAllInflections, getAllInflectionsOOV
app = Flask(__name__)

# getLemma(word, upos, lemmatize_oov=True)
@app.route('/api/getLemma', methods=['GET', 'POST'])
def api_getLemma():
    content = request.get_json()
    result = getLemma( content['word'], content['upos'], content['lemmatize_oov'])
    return jsonify(result)

# getAllLemmas(word, upos=None)
@app.route('/api/getAllLemmas', methods=['GET', 'POST'])
def api_getAllLemmas():
    content = request.json
    result = getAllLemmas( content['word'], content['upos'])
    return jsonify(result)

# getAllLemmasOOV(word, upos)
@app.route('/api/getAllLemmasOOV', methods=['GET', 'POST'])
def api_getAllLemmasOOV():
    content = request.json
    result = getAllLemmasOOV( content['word'], content['upos'])
    return jsonify(result)

# isTagBaseForm(tag)
@app.route('/api/isTagBaseForm', methods=['GET', 'POST'])
def api_isTagBaseForm():
    content = request.json
    result = isTagBaseForm( content['tag'] )
    return jsonify(result)

# ---------------

# getInflection(lemma, tag, inflect_oov=True)
@app.route('/api/getInflection', methods=['GET', 'POST'])
def api_getInflection():
    content = request.json
    result = getInflection( content['lemma'], content['tag'], content['inflect_oov'])
    return jsonify(result)

# getAllInflections(lemma, upos=None)
@app.route('/api/getAllInflections', methods=['GET', 'POST'])
def api_getAllInflections():
    content = request.json
    result = getAllInflections( content['lemma'], content['upos'])
    return jsonify(result)

# getAllInflectionsOOV(lemma, upos)
@app.route('/api/getAllInflectionsOOV', methods=['GET', 'POST'])
def api_getAllInflectionsOOV():
    content = request.json
    result = getAllInflectionsOOV( content['lemma'], content['upos'])
    return jsonify(result)

# Instructions/help
@app.route('/')
def api_help():
    return 'API for lemminflect, closely following these docs: https://lemminflect.readthedocs.io/en/latest/inflections/'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')