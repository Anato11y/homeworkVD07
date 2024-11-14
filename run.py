from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создание таблиц при первом запуске
    app.run(debug=True)
