pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                '''
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Start FastAPI Application') {
            steps {
                sh '''
                # Kill any existing FastAPI instance
                pkill -f "uvicorn main:app" || true
                
                # Start FastAPI and redirect logs
                . venv/bin/activate
                nohup uvicorn main:app --host 0.0.0.0 --port 8000 > fastapi.log 2>&1 &
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                
                # Run tests with detailed logs and save to pytest.log
                pytest -s --junitxml=test-results.xml | tee pytest.log
                '''
            }
        }
        stage('Post-Test Cleanup') {
            steps {
                sh '''
                # Optional: Kill FastAPI instance after tests
                pkill -f "uvicorn main:app" || true
                '''
            }
        }
    }
    post {
        always {
            // Archive important logs and test results
            archiveArtifacts artifacts: 'pytest.log, fastapi.log, test-results.xml', allowEmptyArchive: true
        }
        cleanup {
            sh '''
            # Clean up virtual environment
            rm -rf venv
            '''
        }
    }
}
