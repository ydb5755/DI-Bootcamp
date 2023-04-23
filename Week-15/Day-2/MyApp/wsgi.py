from app import create_app, populate_categories


app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # populate_categories()
        app.run(debug=True)
