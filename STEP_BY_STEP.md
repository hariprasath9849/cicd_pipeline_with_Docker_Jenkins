Step-by-step: install, run, and view output (Windows + PowerShell)

Option A: Run locally (no Docker, no Jenkins)

1) Install Python 3.11+ and Git
   - Python: https://www.python.org/downloads/windows/
   - Git: https://git-scm.com/download/win
   - After install, reopen PowerShell so PATH updates.

2) Clone the repo
```powershell
git clone https://github.com/Hariprasath76/Hello_World_Python.git
cd Hello_World_Python
```

3) Update environment values
   - Open `.env` and set `SECRET_KEY`.
   - If you access the app via an IP, add it to `ALLOWED_HOSTS` (comma-separated).

4) Create and activate a virtual environment
```powershell
python -m venv venv
venv\Scripts\activate
```

5) Install dependencies
```powershell
pip install -r requirements.txt
```

6) Run database migrations
```powershell
python manage.py migrate
```

7) Start the Django dev server
```powershell
python manage.py runserver
```

8) See the output in your browser
   - Open http://127.0.0.1:8000/
   - Enter your name and submit.
   - Expected output:
     "Hello <Name>! Welcome to the One Data Solution."

Option B: Run using Docker + Jenkins (local CI/CD)

Prerequisites
- Docker Desktop (running)
- Git

1) Start Jenkins in Docker
```powershell
docker volume create jenkins_home
docker run -d --name jenkins `
  -p 8080:8080 -p 50000:50000 `
  -v jenkins_home:/var/jenkins_home `
  -v /var/run/docker.sock:/var/run/docker.sock `
  jenkins/jenkins:lts
```

2) Get the initial admin password
```powershell
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```
   - Open http://localhost:8080
   - Paste the password and complete the setup wizard.

3) Install required Jenkins plugins
   - Git
   - Pipeline
   - Docker Pipeline
   - Email Extension

4) Create a Pipeline job
   - New Item -> Pipeline
   - SCM: Git
   - Repository URL: https://github.com/Hariprasath76/Hello_World_Python.git
   - Branch: main
   - Script Path: Jenkinsfile
   - Save -> Build Now

5) Verify the container is running
```powershell
docker ps
```

6) See the output in your browser
   - Open http://localhost:8000/
   - Enter your name and submit.
   - Expected output:
     "Hello <Name>! Welcome to the One Data Solution."
