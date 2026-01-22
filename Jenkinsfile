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
    }

    post {
    success {
        mail(
            to: 'hariprasathawsdevops@gmail.com',
            subject: "SUCCESS ✅: ${JOB_NAME} #${BUILD_NUMBER}",
            mimeType: 'text/html',
            body: """
            <html>
              <body>
                <p>
                  Hi,<br/><br/>
                  Your job <b>${JOB_NAME}</b> status is
                  <span style="color:green; font-weight:bold;">SUCCESS</span>
                </p>

                <p>
                      <b>Build Status:</b>
                      <span style="
                            background-color: green;
                            color: white;
                            font-weight: bold;
                            padding: 4px 10px;
                            border-radius: 4px;
                            display: inline-block;
                      ">
                        SUCCESS
                      </span>
                    </p>


                <p>
                  <b>Job:</b> ${JOB_NAME}<br/>
                  <b>Build Number:</b> ${BUILD_NUMBER}<br/>
                  <b>Build URL:</b>
                  <a href="${BUILD_URL}">${BUILD_URL}</a>
                </p>

                <br/>
              </body>
            </html>
            """
        )
    }

    failure {
        mail(
            to: 'hariprasathawsdevops@gmail.com',
            subject: "FAILED ❌: ${JOB_NAME} #${BUILD_NUMBER}",
            mimeType: 'text/html',
            body: """
            <html>
              <body>
                <p>
                  Hi,<br/><br/>
                  Your job <b>${JOB_NAME}</b> status is
                  <span style="color:red; font-weight:bold;">FAILED</span>
                </p>

               <p>
                  <b>Build Status:</b>
                  <span style="
                        background-color: red;
                        color: white;
                        font-weight: bold;
                        padding: 4px 10px;
                        border-radius: 4px;
                        display: inline-block;
                  ">
                    FAILED
                  </span>
                </p>

                <p>
                  <b>Job:</b> ${JOB_NAME}<br/>
                  <b>Build Number:</b> ${BUILD_NUMBER}<br/>
                  <b>Build URL:</b>
                  <a href="${BUILD_URL}">${BUILD_URL}</a>
                </p>

                <br/>
              </body>
            </html>
            """
            )
        }
    }
}
