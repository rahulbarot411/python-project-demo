from django.shortcuts import render, redirect
from pymongo import MongoClient

from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from pymongo import MongoClient
import bcrypt


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email").strip()
        password = request.POST.get("password").strip()

        # Connect to MongoDB
        client = MongoClient("mongodb://localhost:27017/")
        db = client["Updatedjson"]
        collection = db["users"]

        # Find the user by email
        user = collection.find_one({"email": email})

        if user and bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
            if user.get("role") == "admin":
                # Successful admin login
                request.session['user_email'] = email
                return redirect('all-blog')
            else:
                messages.error(request, "Access restricted to admin users.")
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'login.html')