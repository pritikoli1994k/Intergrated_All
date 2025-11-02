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
               bat 'docker container prune -f'
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
