pipeline {
    agent any
    stages {
        stage('Build Code') {
            steps {
                 // Checkout code from the pre-configured SCM
                checkout scm
                // Navigate to the src directory and run make commands
                sh '''
                    cd src
                    make clean
                    make              
                '''
            }
        }
        stage('Scenarios Generation') {
            steps {
                //open the os-shell 
                sh '''
                    
                    cd Startupfiles
                    python3 Generate_Startup.py
                    cd ..
                    //creating the testrun variations
                    for file in Startupfiles/*
                    do
                          src/CarMaker.linux64 "$file" -v -screen -dstore
                    done
                '''
            }
        }
    }
}
