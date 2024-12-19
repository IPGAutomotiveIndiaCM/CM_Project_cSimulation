pipeline {
    agent any
    stages {
        stage('Build Code') {
            steps {
                withCredentials([usernamePassword(credentialsId: '6911c2fc-83c4-48f1-9829-5d81e833b3d0', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]) {
                    // Checkout code
                    checkout scm
                    sh '''
                    # Configure Git
                    git checkout master
                    git config user.email "dhrithi.dk@ipg-automotive.com"
                    git config user.name "IPGAutomotiveIndiaCM"
                   
                    # Set the remote URL with credentials
                    git remote set-url origin https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/${GIT_USERNAME}/CM_Project.git
                   
                    # Pull latest changes
                    git pull origin master
 
                    # Build code
                    cd src
                    make clean
                    make
                    '''
                }
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
                git push -u origin master
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
