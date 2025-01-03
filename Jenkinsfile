pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        APP_HOST = '0.0.0.0'
        APP_PORT = '8000'
        APP_LOG = 'app.log'
    }

    stages {
        stage('Clone Repository') {
            steps {
                withChecks('Clone Repository') {
                    publishChecks name: 'Clone Repository', status: 'IN_PROGRESS', summary: 'Cloning the repository.'
                    git credentialsId: 'jenkinsw4', url: 'https://github.com/songphuongle/fastapi-jenkins.git'
                    publishChecks name: 'Clone Repository', status: 'COMPLETED', conclusion: 'SUCCESS', summary: 'Repository cloned successfully.'
                }
            }
        }

        stage('Cleanup') {
            steps {
                withChecks('Cleanup') {
                    publishChecks name: 'Cleanup', status: 'IN_PROGRESS', summary: 'Cleaning up any existing processes.'
                    script {
                        sh '''
                        pkill -f "uvicorn main:app" || true
                        rm -rf ${VENV_DIR} ${APP_LOG}
                        '''
                    }
                    publishChecks name: 'Cleanup', status: 'COMPLETED', conclusion: 'SUCCESS', summary: 'Cleanup completed successfully.'
                }
            }
        }

        stage('Set Up Python Environment') {
            steps {
                withChecks('Set Up Python Environment') {
                    publishChecks name: 'Set Up Python Environment', status: 'IN_PROGRESS', summary: 'Setting up Python environment.'
                    script {
                        sh '''
                        python3 -m venv ${VENV_DIR}
                        . ${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        '''
                    }
                    publishChecks name: 'Set Up Python Environment', status: 'COMPLETED', conclusion: 'SUCCESS', summary: 'Python environment set up successfully.'
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
                        pytest --junitxml=results.xml --cov=your_module --cov-report=xml || exit 1
                        '''
                    }
                    junit 'results.xml' // Publish test results in Jenkins
                    publishChecks name: 'Run Tests', status: 'COMPLETED', conclusion: 'SUCCESS', summary: 'All tests passed successfully.'
                }
            }
        }

        stage('Run API') {
            steps {
                withChecks('Run API') {
                    publishChecks name: 'Run API', status: 'IN_PROGRESS', summary: 'Running the API application.'
                    script {
                        sh '''
                        . ${VENV_DIR}/bin/activate
                        nohup uvicorn main:app --host ${APP_HOST} --port ${APP_PORT} > ${APP_LOG} 2>&1 &
                        sleep 5 // Allow the app to start
                        python -c "
import requests
import sys
try:
    response = requests.get(f'http://${APP_HOST}:${APP_PORT}/')
    if response.status_code == 200:
        print('API is healthy.')
    else:
        print('API health check failed with status code:', response.status_code)
        sys.exit(1)
except Exception as e:
    print('API health check failed with error:', str(e))
    sys.exit(1)
                        "
                        '''
                    }
                    publishChecks name: 'Run API', status: 'COMPLETED', conclusion: 'SUCCESS', summary: 'API is running successfully.'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded.'
            script {
                publishChecks name: 'Pipeline Execution', status: ChecksStatus.COMPLETED, conclusion: ChecksConclusion.SUCCESS, summary: 'Pipeline completed successfully.'
            }
        }
        failure {
            echo 'Pipeline failed.'
            script {
                publishChecks name: 'Pipeline Execution', status: ChecksStatus.COMPLETED, conclusion: ChecksConclusion.FAILURE, summary: 'Pipeline encountered an error.'
            }
        }
    }
}
