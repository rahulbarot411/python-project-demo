import bcrypt
from pymongo import MongoClient

# def create_admin_user(email, password):
#     # Connect to MongoDB
#     client = MongoClient("mongodb://localhost:27017/")
#     db = client["Updatedjson"]
#     collection = db["admin_access"]

#     # Hash the password
#     hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

#     # Check if the admin user already exists
#     if collection.find_one({"email": email}):
#         print("Admin user with this email already exists.")
#         return

#     # Insert admin user into the database
#     admin_user = {
#         "email": email,
#         "password": hashed_password.decode('utf-8'),  # Store as a string
#         "role": "admin",  # Indicate this user is an admin
#     }
#     collection.insert_one(admin_user)
#     print("Admin user created successfully!")

# create_admin_user("admin@example.com", "admin123")


def check_or_create_admin(email, password):
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Updatedjson"]
    collection = db["admin_credentials"]  # New collection for admin credentials

    # Find the admin by email
    admin = collection.find_one({"email": email})

    if not admin:
        print("Admin not found! Creating admin user...")

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Insert the new admin user
        new_admin = {
            "email": email,
            "password": hashed_password.decode('utf-8')
        }
        collection.insert_one(new_admin)
        print("Admin user created successfully!")
        return True

    # Compare the entered password with the stored hashed password
    stored_hashed_password = admin["password"].encode('utf-8')  # Get the hashed password from MongoDB

    if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
        print("Login successful!")
        return True
    else:
        print("Invalid password!")
        return False

# Test the function
check_or_create_admin("admin@example.com", "admin123")

