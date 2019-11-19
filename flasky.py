from app import create_app, db
import os
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# with app.app_context():
#     db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="4000", debug=True)