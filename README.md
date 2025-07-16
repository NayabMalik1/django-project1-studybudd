
## **Comment Feature — Room Conversations in Real Time**

This feature enables users to engage in discussions within individual rooms by posting and viewing messages in a clean and organized format.

###  Key Highlights

* Displays a room’s **title and description**.
* Shows a list of all comments/messages posted in the room.
* Each message displays:

  * The **username** of the sender.
  * The **relative timestamp** (e.g., `5 minutes ago`).
  * The **message content**.
* Fully integrated with Django ORM using reverse model relationships.

---

### 🧩 Tech Stack

* **Backend:** Django, Python
* **Frontend:** HTML, Django Templates
* **Database:** SQLite (can be upgraded to PostgreSQL/MySQL)
* **Template Filter:** `timesince` from `django.contrib.humanize` for friendly timestamps

---




###  Security & Validation

* All messages are associated with authenticated users.
* Messages are fetched based on the selected room ID (`pk`) ensuring isolation.

---

###  Future Enhancements

* Live chat using WebSockets (Django Channels).
* Emoji support and rich-text formatting.
* Edit/delete functionality for messages.
* Real-time notifications.


