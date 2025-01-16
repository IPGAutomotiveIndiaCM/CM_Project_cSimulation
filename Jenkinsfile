pipeline {
    agent any
    environment {
      IPGHOME = "/opt/ipg/"
    }
    stages {
        stage('Build Code') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'cSimulation', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]) {
                    // Checkout code
                    checkout scm
                    sh '''
                    # Configure Git
                    git clean -fd
                    git checkout master
                    git config user.email "dhrithi.dk@ipg-automotive.com"
                    git config user.name "IPGAutomotiveIndiaCM"
                   
                    # Set the remote URL with credentials
                    git remote set-url origin https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/${GIT_USERNAME}/CM_Project_cSimulation.git
                   
                    # Pull latest changes
                    git pull origin master
 
                    # Build code
                    cd src
                    make clean
                    ls -la
                    pwd
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
                
                '''
                
            }
        }
        stage('Simulation Running') {
            steps {
                // Placeholder for the simulation running commands
                sh '''
                    echo "Running ffffthe simulation now... in "
                    # Add your simulation commands here
                    cd "$WORKSPACE"
                    for file in Startupfiles/Startup_Example_*;
                    do
                    
                        src/CarMaker.linux64 "$file" -v -screen -dstore 
                    done
                '''
            }
        }
        stage('Report Evaluation') {
            steps {
                // Placeholder for the simulation running commands
                //call that python3 script
                sh '''
                    echo "Running ffffthe simulation now... in "
                    # Add your simulation commands here
                    python3 -m pip install cmerg
                    cd Startupfiles
                    python3 Generate_Report.py
                '''
            }
        }
    }
}
