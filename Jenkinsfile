pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Cleanup') {
            steps {
                withChecks('Cleanup') {
                    publishChecks name: 'Cleanup', status: 'IN_PROGRESS', summary: 'Cleaning up any existing processes.'
                    script {
                        // Stop any running instance of the application
                        sh 'pkill -f "uvicorn main:app" || true'
                    }
                    publishChecks name: 'Cleanup', status: 'COMPLETED', conclusion: 'SUCCESS', summary: 'Cleanup completed successfully.'
                }
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                withChecks('Set Up Virtual Environment') {
                    publishChecks name: 'Set Up Virtual Environment', status: 'IN_PROGRESS', summary: 'Setting up virtual environment.'
                    script {
                        sh '''
                        python3 -m venv ${VENV_DIR} || true
                        . ${VENV_DIR}/bin/activate
                        pip install --upgrade pip || true
                        '''
                    }
                    publishChecks name: 'Set Up Virtual Environment', status: 'COMPLETED', conclusion: 'SUCCESS', summary: 'Virtual environment setup successfully.'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                withChecks('Install Dependencies') {
                    publishChecks name: 'Install Dependencies', status: 'IN_PROGRESS', summary: 'Installing dependencies.'
                    script {
                        sh '''
                        . ${VENV_DIR}/bin/activate
                        pip install -r requirements.txt
                        '''
                    }
                    publishChecks name: 'Install Dependencies', status: 'COMPLETED', conclusion: 'SUCCESS', summary: 'Dependencies installed successfully.'
                }
            }
        }

        stage('Run Tests') {
            steps {
                withChecks('Run Tests') {
                    publishChecks name: 'Run Tests', status: 'IN_PROGRESS', summary: 'Running tests.'
                    script {
                        sh '''
                        . ${VENV_DIR}/bin/activate
                        pytest --junitxml=test-results.xml
                        '''
                    }
                    publishChecks name: 'Run Tests', status: 'COMPLETED', conclusion: 'SUCCESS', summary: 'All tests passed successfully.'
                }
            }
        }

        stage('Run Application') {
            steps {
                withChecks('Run Application') {
                    publishChecks name: 'Run Application', status: 'IN_PROGRESS', summary: 'Running the application.'
                    script {
                        sh '''
                        . ${VENV_DIR}/bin/activate
                        nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
                        '''
                    }
                    publishChecks name: 'Run Application', status: 'COMPLETED', conclusion: 'SUCCESS', summary: 'Application is running successfully.'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo 'Pipeline succeeded.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
