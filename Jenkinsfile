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
                bat '''
                for /F %i in ('docker ps -aq') do docker rm -f %i
                '''
            }
        }

        stage('Build Image') {
            steps {
                bat 'docker build -t myapp .'
            }
        }

        stage('Create Container') {
            steps {
                bat 'docker run -d -p 8501:8501 myapp'
            }
        }
    }
}
