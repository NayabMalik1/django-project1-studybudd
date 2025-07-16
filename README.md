### 💬 **Feature: Comments and Participants List**

This feature enhances room interaction by:

- ✅ Allowing authenticated users to post comments in real-time.
- ✅ Displaying all previous comments with timestamps (e.g., "7 minutes ago").
- ✅ Listing all active participants in the room.
- ✅ Secure access with user authentication (`@login_required`).

**Location:**  
- Views: `room()` in `views.py`  
- Template: `room.html`  
- Models: `Message`, `Room` (related via ForeignKey)

**Usage:**  
- Users must be logged in to post comments.
- All messages are stored in the `Message` model and displayed in the room.


