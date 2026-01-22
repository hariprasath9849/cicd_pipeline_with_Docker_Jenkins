CI/CD with Jenkins + Docker (Local)

This repo contains a simple Django app and a Jenkins pipeline to:
- Checkout code from GitHub
- Build a Docker image
- Run a container
- Send email notifications on build result

Project Structure

onedata_project/
|-- manage.py
|-- Task/                 # Django project folder
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
`-- greet/                # App folder
    |-- __init__.py
    |-- views.py
    |-- urls.py
    |-- forms.py
    `-- templates/
        `-- greet.html

App Output
Hello <Name>! Welcome to the One Data Solution.

Prerequisites
- Docker Desktop (running)
- Git
- A GitHub account with access to the repo

Step-by-step (Human Commands)

1) Clone the repo (local dev or for Jenkins workspace)
```powershell
git clone https://github.com/Hariprasath76/Hello_World_Python.git
cd Hello_World_Python
```

2) Run Jenkins locally using Docker
```powershell
docker volume create jenkins_home
docker run -d --name jenkins `
  -p 8080:8080 -p 50000:50000 `
  -v jenkins_home:/var/jenkins_home `
  -v /var/run/docker.sock:/var/run/docker.sock `
  jenkins/jenkins:lts
```
Note: On Windows with Docker Desktop (Linux containers), the Docker socket mapping above works in most setups.
If Docker commands fail inside Jenkins, use a Docker-enabled Jenkins image or configure Docker Desktop
to allow the Jenkins container to access the daemon.

3) Get the Jenkins admin password
```powershell
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```
Open http://localhost:8080 and complete the setup wizard.

4) Install Jenkins plugins
Required:
- Git
- Pipeline
- Docker Pipeline
- Email Extension (for notifications)
Optional:
- Blue Ocean
- Slack Notification

5) Create a Pipeline job
- New Item -> Pipeline
- SCM: Git
- Repository URL: https://github.com/Hariprasath76/Hello_World_Python.git
- Branch: main
- Script Path: Jenkinsfile
- Save -> Build Now

6) Verify container is running
```powershell
docker ps
```
Open http://localhost:8000

Local Run (without Jenkins)
```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Open http://127.0.0.1:8000/

Jenkins Pipeline (What It Does)
The Jenkinsfile runs:
- Checkout (GitHub)
- Build Docker image
- Run Docker container
- Send email notification (post section)

Optional: Add a Test Stage
If you want tests in the pipeline, add this stage before Docker build:
```groovy
stage('Test') {
    steps {
        sh 'pip install -r requirements.txt'
        sh 'python manage.py test'
    }
}
```

Email Notification Setup
Jenkins -> Manage Jenkins -> Configure System -> Extended E-mail Notification:
- SMTP server (Gmail, Office365, etc.)
- Credentials
- Default content and recipients
The current Jenkinsfile uses `emailext` in the `post` block.

Slack Notification (Bonus)
1) Install "Slack Notification" plugin
2) Configure Slack workspace and credentials
3) Add a post step like:
```groovy
post {
    always {
        slackSend(channel: '#builds', message: "Build ${currentBuild.currentResult}: ${env.JOB_NAME} #${env.BUILD_NUMBER}")
    }
}
```

Example Output
Enter your name -> HARIPRASATH
Output:
Hello HARIPRASATH! Welcome to the One Data Solution.
