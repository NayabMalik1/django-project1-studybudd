

## 🔐 **Feature: User Authentication & Registration**

This feature adds full authentication support using Django's built-in user model. It allows users to register, log in, log out, and restricts access to certain actions like room creation and editing to authenticated users only.

---

### ✅ **Implemented Functionalities**

#### 🔑 **User Login**

* **View:** `loginPage`
* **Mechanism:** Uses `authenticate()` and `login()` from `django.contrib.auth`
* **Error Handling:** Invalid credentials show proper error via `messages.error()`
* **Redirect:** On success, redirects to home page

#### 🚪 **User Logout**

* **View:** `logoutUser`
* **Mechanism:** Uses Django’s `logout()` method
* **Redirect:** Returns to home page after logging out

#### 📝 **User Registration**

* **View:** `registerPage`
* **Mechanism:** Uses Django’s `UserCreationForm` and `save()` to register new users
* **Validation:** Checks if username already exists
* **Login on Success:** Automatically logs in the user after registration
* **Redirect:** Redirects to home page

#### 🔐 **Access Control**

* **Protected Views:** `@login_required(login_url='login')` used for:

  * Creating a room
  * Updating a room
  * Deleting a room
* **Authorization Check:** Users can only update/delete their own rooms:

  ```python
  if request.user != room.host:
      return HttpResponse("You are not allowed here!")
  ```

---

### 📄 **Templates Modified or Created**

| Template File         | Purpose                                                               |
| --------------------- | --------------------------------------------------------------------- |
| `login_register.html` | Combined login & registration form                                    |
| `navbar.html`         | Shows "Login", "Logout", and user info dynamically                    |
| `room_form.html`      | Used for both creating and updating rooms (restricted to owners only) |
| `delete.html`         | Delete confirmation restricted to the room owner                      |

---

### 🔐 **Security **

* ✅ Only logged-in users can manage rooms
* ✅ Passwords securely stored using Django's auth system
* ✅ Prevents unauthorized content access and editing
* ✅ Auto-login after registration for smoother user experience

---

### 🌐 **Related URLs for Testing (Localhost)**

| URL                                                   | Description                  |
| ----------------------------------------------------- | ---------------------------- |
| [`/login/`](http://127.0.0.1:8000/login/)             | User login                   |
| [`/logout/`](http://127.0.0.1:8000/logout/)           | User logout                  |
| [`/register/`](http://127.0.0.1:8000/register/)       | New user registration        |
| [`/create-room/`](http://127.0.0.1:8000/create-room/) | Create room (login required) |

