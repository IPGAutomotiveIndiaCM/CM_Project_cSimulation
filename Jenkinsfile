pipeline {
    node('label'){
    // now you are on slave labeled with 'label'
    def workspace = WORKSPACE
    // ${workspace} will now contain an absolute path to job workspace on slave

    workspace = env.WORKSPACE
    // ${workspace} will still contain an absolute path to job workspace on slave

    // When using a GString at least later Jenkins versions could only handle the env.WORKSPACE variant:
    echo "Current workspace is ${env.WORKSPACE}"

    // the current Jenkins instances will support the short syntax, too:
    echo "Current workspace is $WORKSPACE"

}
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
                    for file in Startupfiles/*
                    do
                          src/CarMaker.linux64 "$file" -v -screen -dstore
                    done
                '''
            }
        }
        stage('Simulation runing') {
            steps {
                //open the os-shell 
                sh '''
                    
                '''
            }
        }
    }
}
