
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
        disableConcurrentBuilds()
    }

    environment {
        IMAGE_NAME = 'studentforms'
        SERVER_IP = '192.168.56.102'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build \
                      -t ${IMAGE_NAME}:${BUILD_NUMBER} .
                '''
            }
        }

        stage('Save Docker Image') {
            steps {
                sh '''
                    docker save \
                      -o studentforms.tar \
                      ${IMAGE_NAME}:${BUILD_NUMBER}
                '''
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sshagent(credentials: ['ubuntu-deploy-key']) {
                    sh '''
                        ansible-playbook \
                          -i ansible/inventory_lab5.ini \
                          ansible/deploy_docker.yml \
                          -e "image_archive=${WORKSPACE}/studentforms.tar" \
                          -e "image_tag=${BUILD_NUMBER}"
                    '''
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    curl --fail \
                      http://${SERVER_IP}:5000/
                '''
            }
        }
    }

    post {
        always {
            sh 'rm -f studentforms.tar'
        }
    }
}
