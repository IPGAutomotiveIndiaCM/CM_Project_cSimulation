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
                sh '''
                cd Startupfiles
                python3 Generate_Startup.py
                cd "$WORKSPACE"
                for file in Startupfiles/*
                do
                    src/CarMaker.linux64 "$file" -v -screen -dstore
                done
                timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
                cd "$WORKSPACE/cSimulation/CM_Project/SimOutput"
                git add .
                git commit -m "SimOutput results update: $timestamp"
                git push
                '''
            }
        }
        stage('Simulation Running') {
            steps {
                // Placeholder for the simulation running commands
                sh '''
                    echo "Running the simulation now..."
                    # Add your simulation commands here
                '''
            }
        }
    }
}
 
