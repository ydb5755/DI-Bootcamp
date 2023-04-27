from app import create_app


app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # from app.pop import create_planets_cards, create_starships_cards, create_vehicles_cards, create_people_cards
        # create_people_cards()
        # create_vehicles_cards()
        # create_starships_cards()
        # create_planets_cards()
        app.run(debug=True)