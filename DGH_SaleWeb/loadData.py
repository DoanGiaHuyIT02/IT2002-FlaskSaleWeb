import json
from DGH_SaleWeb import app


def load_categories():
    with open('%s/data/dataJson.json' % app.root_path, encoding='utf 8') as f:
        return json.load(f)


def load_product():
    with open('%s/data/product.json' % app.root_path, encoding='utf 8') as f:
        return json.load(f)