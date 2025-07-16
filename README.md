

###  **Feature: Theme Customization**

This feature enhances the visual appeal and layout of the StudyBuddy web application by improving the structure, style, and responsiveness of various pages.

#### ✅ **Changes Introduced**

* Refactored HTML templates to align with consistent layout using utility classes.
* Redesigned **room list**, **recent activity**, and **topic sections** with better spacing and structure.
* Connected custom `main.css` using `{% static %}` correctly.
* Used modern design patterns (3-column grid layout) for homepage and profile pages.
* Improved the mobile menu and avatar structure.
* Aligned typography and colors for better readability.

#### 📁 Affected Files

* `base/home.html`
* `base/feed_component.html`
* `base/topics_component.html`
* `base/navbar.html`
* `base/profile.html`
* `static/styles/main.css`
* `main.html` (template wrapper)

#### 💡 How to Use

1. Switch to the branch:

   ```bash
   git checkout feature/theme-customization
   ```

2. Run your Django server:

   ```bash
   python manage.py runserver
   ```

3. Visit `http://127.0.0.1:8000/` to see the updated layout and styles.

#### 📌 Notes

* No backend logic is altered.
* Only formatting, layout, and static file configuration is updated.
* Compatible with existing features and routes.

