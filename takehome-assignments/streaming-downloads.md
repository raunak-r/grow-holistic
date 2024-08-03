# Streaming Downloads
Your task is to set up a project that accomplishes a streaming download architecture in Java.

## Project Requirements:
Frontend:
```
Create a small frontend project in Angular or React with a single homepage.
The homepage should contain a single button with the text "Download".
```

Backend:
```
Set up a Java backend that handles the download request.
The backend should have an offline zip file of more than 2000 MB (you can source any large zip file).
Upon receiving a GET request triggered by clicking the "Download" button, the backend should start streaming the zip file to the client.
```

Streaming Download:
```
Implement the streaming download so that the client can start receiving the file immediately without waiting for the entire file to be ready.
```

Notification on Completion:
```
On completion of the download, the Java backend should send a notification to the client with the message "Success".
```

## Deliverable:
```
Create a repository on your personal GitHub and create two folders, one each for the backend and frontend in the same repo with all the code.
You are expected to have a minimum of 5 commits, demonstrating the growth of the code over the course of your project.
```

## Follow-up Questions:
```
How would you handle the scenario where the client disconnects during the download?
What strategies would you use to ensure the download process is efficient and doesn't overwhelm the server?
How would you ensure the integrity of the downloaded file?
How would you handle errors during the download process and notify the client appropriately?
```
