from app import app

@app.route('/product/list')
def product():
    return " this is product page"