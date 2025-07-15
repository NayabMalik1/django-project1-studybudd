## ✏️ **Feature: Update Room**

This branch adds functionality to update existing discussion rooms using Django forms.

---

### 🔧 What This Feature Includes:

- View function to edit existing rooms.
- Reuses `RoomForm` for both create and update.
- Form pre-filled with the room’s current data.
- Room updates saved and redirected to homepage.

---

### 🧩 Files Modified:
- `views.py`
- `urls.py`
- `home.html` (Edit link added beside each room)

---

### 🔗 URLs:
| Page            | Description                       | Link (Localhost)                                   |
|------------------|-----------------------------------|----------------------------------------------------|
| Edit Room Page   | Edit room by ID                   | `http://127.0.0.1:8000/update-room/<room_id>/`     |
| Home Page        | Has edit buttons next to rooms    | [http://127.0.0.1:8000/](http://127.0.0.1:8000/)    |

---

### 💡 How to Use:

1. Navigate to the home page.
2. Click **Edit** next to any room.
3. Modify the form and click **Submit**.
4. Room updates will reflect on the home page.

