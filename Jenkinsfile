pipeline {
    agent any

    stages {

        stage('Pull Code') {
            steps {
                echo 'Fetching latest code from GitHub'
                git 'https://github.com/VPatil3155/event-registration-devops1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image'
                bat 'docker build -t flask-event .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker stop flask-container || exit 0'
                bat 'docker rm flask-container || exit 0'
            }
        }

        stage('Deploy Container') {
            steps {
                echo 'Running Docker container'
                bat 'docker run -d -p 5000:5000 --name flask-container flask-event'
            }
        }
    }
}