pipeline {
    agent any

    environment {
        IMAGE_NAME = "hariprasath9849/hello-world-python"
        CONTAINER_NAME = "hello_app"
    }

    stages {

        stage('Clone GitHub Repo') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/hariprasath9849/cicd_pipeline_with_Docker_Jenkins.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                      echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                      docker push $IMAGE_NAME:latest
                    '''
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                  docker rm -f $CONTAINER_NAME || true
                  docker run -d -p 8000:8000 --name $CONTAINER_NAME $IMAGE_NAME:latest
                '''
            }
        }

         post {
        success {
            emailext(
                to: 'hariprasathawsdevops@gmail.com',
                subject: "SUCCESS: $PROJECT_NAME #$BUILD_NUMBER",
                body: """
                <h3>Build SUCCESS</h3>
                <p>Project: $PROJECT_NAME</p>
                <p>Build: #$BUILD_NUMBER</p>
                <p>URL: <a href="$BUILD_URL">$BUILD_URL</a></p>
                """
            )
        }

        failure {
            emailext(
                to: 'hariprasathawsdevops@gmail.com',
                subject: "FAILED: $PROJECT_NAME #$BUILD_NUMBER",
                body: """
                <h3>Build FAILED</h3>
                <p>Project: $PROJECT_NAME</p>
                <p>Build: #$BUILD_NUMBER</p>
                <p>Check logs: <a href="$BUILD_URL">$BUILD_URL</a></p>
                """
            )
        }
    }
}