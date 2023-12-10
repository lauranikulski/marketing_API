from flask import Flask, current_app
from app import db, User 

add_first_user = User(id=1, email='first@example.com', password='myverysecretpassword')

with current_app.app_context():
    try:
        db.session.add(add_first_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {str(e)}")

# can update using query
# eg update_1 = User.query.get(1)
# User.email = 'anotheremail@example.com'
# can delete, also using query
# db.session.delete(User.query.get(1))


first_user_added = db.query.all()
print(first_user_added)
