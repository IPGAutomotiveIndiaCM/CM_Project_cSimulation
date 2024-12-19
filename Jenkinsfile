pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                // Checkout code from the pre-configured SCM
                checkout scm
            }
        }
        stage('Build Code') {
            steps {
                // Navigate to the src directory and run make commands
                sh '''
                    cd src
                    make clean
                    make
                    cd Startupfiles
                    python3 Generate_Startup.py
                '''
            }
        }
    }
}
