pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                script {
                    // Clone the repository
                    checkout scm
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies
                    sh 'pip3 install --user -r requirements.txt'
                }
            }
        }
        stage('Run API') {
            steps {
                script {
                    // Run FastAPI application
                    sh 'nohup uvicorn main:app --host 0.0.0.0 --port 8000 &'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run the test suite
                    sh 'pytest test_main.py'
                }
            }
        }
    }
    post {
        always {
            // Publish the test status using GitHub Checks plugin
            publishChecks name: 'API Tests', summary: 'Tests Completed'
        }
        failure {
            // Send a message or take any action on failure
            echo 'Build failed. Check logs for details.'
        }
        success {
            // Action on success
            echo 'Build succeeded.'
        }
    }
}
