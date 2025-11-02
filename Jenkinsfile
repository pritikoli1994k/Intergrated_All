pipeline{
    agent any
    stages{
        stage("checkput code")
        {
            steps{
                    git url:"https://github.com/pritikoli1994k/Intergrated_All.git" ,branch :main 
                 }

        }
        stage("Build image")
        {
            steps{
                   stage('Build') {
                         main.sh('docker build -t myapp .')
                    }   
→ Jenkin
                 }

        }

        stage("create container")
        {
            steps{
                    bat 'docker run -d -p 8501:8501 myimage'
                 }

        }

         }
    }
