pipeline {
    agent any
    stages {
        stage('Build Code') {
            steps {
                // Checkout code from the pre-configured SCM
                checkout scm
                // Navigate to the src directory and run make commands
                sh '''
                    git checkout master
                    git config user.email "dhrithi.dk@ipg-automotive.com"
                    git config user.name "IPGAutomotiveIndiaCM"
                    git remote set-url origin https://IPGAutomotiveIndiaCM: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@github.com/IPGAutomotiveIndiaCM/CM_Project.git
                                         
                    git pull origin master
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
                timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
                git add .
                git commit -m "SimOutput results update: $timestamp"
                git push https://IPGAutomotiveIndiaCM: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@github.com/IPGAutomotiveIndiaCM/CM_Project.git
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
 
 
