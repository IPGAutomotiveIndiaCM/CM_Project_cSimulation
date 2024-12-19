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
                    cd ..
                    cd Startupfiles
                    python3 Generate_Startup.py
                    cd ..
                    
                    for file in Startupfiles/*
                    do
                          src/CarMaker.linux64 "$file" -v -screen -dstore
                    done
                    
                '''
            }
        }
    }
}
