import io.jenkins.plugins.checks.api.ChecksStatus
import io.jenkins.plugins.checks.api.ChecksConclusion

pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git credentialsId: 'jenkinsw4', url: 'https://github.com/songphuongle/fastapi-jenkins.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run API') {
            steps {
                sh '''
                source venv/bin/activate
                nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pytest --junitxml=results.xml
                '''
            }
        }
    }

    post {
        success {
            publishChecks name: 'API Tests', status: ChecksStatus.COMPLETED, conclusion: ChecksConclusion.SUCCESS
        }
        failure {
            publishChecks name: 'API Tests', status: ChecksStatus.COMPLETED, conclusion: ChecksConclusion.FAILURE
        }
    }
}
