
### 🔐 **Feature: User Authentication & Access Control**

This feature secures the platform by allowing only registered users to create, update, and delete rooms, and ensures users can only manage their own content.

#### ✅ **Implemented Functionalities:**

* **User Login:**

  * Handled by the `loginPage` view.
  * Uses Django’s `authenticate()` function to validate credentials.
  * Displays error messages for invalid logins using Django's `messages` framework.

* **User Logout:**

  * Handled by the `logoutUser` view.
  * Redirects to the homepage after successful logout.

* **Access Restrictions:**

  * Only authenticated users can:

    * ✅ Create rooms
    * ✅ Update their own rooms
    * ✅ Delete their own rooms
  * Unauthenticated users are redirected to the login page.
  * Users cannot modify rooms created by other users.

* **Authorization Logic:**

  * Secured views with `@login_required(login_url='login')`.
  * Checked user permissions before allowing edits/deletions:

    ```python
    if request.user != room.host:
        return HttpResponse('You are not allowed here!')
    ```

#### 📄 **Associated Templates:**

* `login_register.html` — login form interface
* `navbar.html` — shows login/logout links based on session
* `room_form.html` — used for both creating and updating rooms
* `delete.html` — confirmation prompt for deleting rooms

#### 🔐 **Security Benefits:**

* Prevents unauthorized access and modifications.
* Encourages user accountability by enforcing content ownership.
