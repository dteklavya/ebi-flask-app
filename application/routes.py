from flask import jsonify, request
from flask import current_app as app
from application.models import db, Genes
from application.exceptions import InvalidUsage


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/genes', methods=['GET'])
def find_gene():
    # Get the request parameters
    gene_lookup = request.args.get('lookup', '')
    species = request.args.get('species', '')

    # Raise exception if queries are not of minimum length.
    # Gene lookup is required.
    if not gene_lookup or len(gene_lookup) < 3:
        raise InvalidUsage('Lookup query length must be greater than 2.', status_code=400)

    if species and len(species) < 3:
        raise InvalidUsage('Species query length must be greater than 2.', status_code=400)
    
    if species:
        data = Genes.query.filter(
            Genes.display_label.like("%{}%".format(gene_lookup)), \
            Genes.species.like("%{}%".format(species))
        ).all()
    else:
        data = Genes.query.filter(Genes.display_label.like("%{}%".format(gene_lookup))).all()
    
    result = []
    for i in data:
        row = {
            'gene': i.display_label,
            'species': i.species,
            'stable_id': i.stable_id,
            'location': i.location,
        }
        result.append(row)

    return jsonify(result), 200


@app.route('/', defaults={'path': ''}, methods=['POST', 'PUT', 'PATCH', 'GET'])
@app.route('/<path:path>')
def catch_all(path):
    raise InvalidUsage('Method Not Allowed', status_code=405)
