pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                // Checkout code from the pre-configured SCM
                checkout scm
            }
        }
        stage('List Files') {
            steps {
                // Run ls command to check files
                sh 'ls -la'
            }
        }
    }
}
