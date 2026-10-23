
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
        disableConcurrentBuilds()
    }

    environment {
        IMAGE_NAME = 'studentforms'
        CONTAINER_NAME = 'studentforms-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/EustaceRay/StudentForms.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t studentforms:latest .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                    docker rm -f studentforms-app || true

                    docker run -d \
                      --name studentforms-app \
                      --restart unless-stopped \
                      -p 5000:5000 \
                      studentforms:latest
                '''
            }
        }

        stage('Check Application') {
            steps {
                sh '''
                    sleep 3
                    curl --fail http://127.0.0.1:5000/
                '''
            }
        }
    }
}
