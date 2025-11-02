pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/pritikoli1994k/Intergrated_All.git'
            }
        }

        stage('Cleanup') {
            steps {
                // Remove all stopped containers safely
                bat 'docker container prune -f'
            }
        }

        stage('Build Image') {
            steps {
                bat 'docker build -t myapp .'
            }
        }

        stage('Create Container') {
            steps {
                // Run container from newly built image
                bat 'docker run -d -p 8501:8501 myapp'
            }
        }
    }
}
