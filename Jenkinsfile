pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Build Code') {
            steps {
                script {
                    sh '''
                        cd src
                        make clean
                        make
                        cd ..
                        cd Startupfiles
                        python3 Generate_Startup.py
                        cd ..
                        
                        for file in Startupfiles/*; do
                            src/CarMaker.linux64 "$file" -v -screen -dstore
                            # Move output files to a directory for archiving
                            mv "$file" build_output/
                        done
                    '''
                }
            }
        }
        stage('Archive Files') {
            steps {
                // Archive the output files as build artifacts
                archiveArtifacts artifacts: 'build_output/*', allowEmptyArchive: true
            }
        }
    }
}
