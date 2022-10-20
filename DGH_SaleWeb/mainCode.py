from flask import render_template

from DGH_SaleWeb import app, loadData


@app.route("/")
def index():
    categories = loadData.load_categories()
    product = loadData.load_product()
    return render_template('index.html', categories=categories, product=product)


if __name__ == '__main__':
    app.run(debug=True)