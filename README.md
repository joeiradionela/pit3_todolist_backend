﻿# pit3_todolist_backend
To-Do List App
Overview
The To-Do List app helps users efficiently manage their tasks. Users can create new tasks, edit existing ones, and delete tasks. Additionally, the app offers task filtering by completion status and a dark mode feature for a better user experience.

Key Features
Dark Mode: Toggle between dark and light modes for improved readability.

Task Management:

Add Task: Create new tasks.

Edit Task: Edit the title and details of existing tasks.

Delete Task: Remove tasks from the list.

Task Filters: Filter tasks by completion status (All, Completed, Pending).

API Endpoints
Get All Tasks (GET):
https://pit3-todolist-backend.onrender.com/api/tasks/

Create a Task (POST):
https://pit3-todolist-backend.onrender.com/api/tasks/

Get a Specific Task (GET):
https://pit3-todolist-backend.onrender.com/api/tasks/{id}/

Update a Task (PUT):
https://pit3-todolist-backend.onrender.com/api/tasks/{id}/

Delete a Task (DELETE):
https://pit3-todolist-backend.onrender.com/api/tasks/{id}/

Challenges Faced
Deployment Issues (Render):
There were initial deployment issues due to incorrect configuration in Django's ALLOWED_HOSTS setting. This was resolved by updating ALLOWED_HOSTS to include the correct Render URL.

Installation of Dependencies:
I encountered issues with installing the dependencies from the requirements.txt file. This was solved by verifying the Python environment setup and manually reinstalling the necessary packages.

Solutions
Deployment Issue:
The ALLOWED_HOSTS setting was updated in Django’s settings to match the deployed Render URL, resolving the deployment issue.

Dependency Installation:
Ensured the Python environment was correctly set up and manually installed the dependencies, confirming they were up-to-date and compatible with the project.

Conclusion
The To-Do List app is fully functional and deployed. It provides an efficient way for users to manage tasks, with additional features like task filtering and dark mode. The deployment and setup challenges were successfully addressed, and the app is now live and accessible online.
