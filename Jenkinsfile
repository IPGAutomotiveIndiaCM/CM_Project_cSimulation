pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                // Checkout code from the pre-configured SCM
                checkout scm
            }
        }
        stage('Execute Commands on Remote Server') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'cSimulation-ssh-credentials', 
                    usernameVariable: 'REMOTE_USER', 
                    passwordVariable: 'REMOTE_PASSWORD'
                )]) {
                    script {
                        // Define the remote server details
                        def remote = [:]
                         remote.name = 'remote-server' 
                        remote.host = '192.168.0.105'
                        remote.user = env.REMOTE_USER
                        remote.password = env.REMOTE_PASSWORD
                        remote.allowAnyHosts = true
 
                        // Execute commands on the remote server
                        sshCommand remote: remote, command: '''
                            pwd
                            ls -la
                        '''
                    }
                }
            }
        }
    }
}
