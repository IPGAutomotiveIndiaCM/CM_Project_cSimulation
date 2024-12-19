pipeline {
    agent any
    stages {
        // stage('Build Code') {
        //     steps {
        //         // Checkout code from the pre-configured SCM
        //         checkout scm
        //         // Navigate to the src directory and run make commands
        //         sh '''
        //             cd src
        //             make clean
        //             make
        //         '''
        //     }
        // }
        stage('Scenarios Generation') {
            steps {
                sh '''
                echo "Workspace directory: $WORKSPACE"
                '''
            }
        }
        // stage('Simulation Running') {
        //     steps {
        //         // Placeholder for the simulation running commands
        //         sh '''
        //             echo "Running the simulation now..."
        //             # Add your simulation commands here
        //         '''
        //     }
        // }
    }
}
