pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
        }
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building the Docker image...'
            }
        }
        stage('Test') {
            steps {
                echo 'Running the tests...'
            }
        }
        stage('Results') {
            steps {
                echo 'Tests completed.'
            }
        }
    }
    post {
        always {
            deleteDir()
        }
    }
}

