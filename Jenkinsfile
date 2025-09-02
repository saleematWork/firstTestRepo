pipeline {
    agent any
    
    environment {
        PYTHONPATH = "${WORKSPACE}/src"
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/saleematWork/firstTestRepo.git'
            }
        }
        
        stage('Setup') {
            steps {
              // sh 'python -m venv venv'
              //  sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        
        stage('Lint') {
            steps {
                sh '. venv/bin/activate && flake8 src/ tests/ --max-line-length=88'
            }
        }


        stage('Unit Tests') {
            steps {
                sh '''
                . venv/bin/activate && 
                python -m pytest tests/ -v --cov=src --cov-report=xml:coverage.xml
                '''
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                    publishHTML(target: [
                        allowMissing: false,
                        alwaysLinkToLastBuild: false,
                        keepAll: true,
                        reportDir: 'htmlcov',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report'
                    ])
                }
            }
        }
        
        stage('Integration Tests') {
            steps {
                sh '''
                . venv/bin/activate && 
                python -m pytest tests/test_integration.py -v
                '''
            }
        }
        
        stage('Generate Reports') {
            steps {
                sh '. venv/bin/activate && coverage xml'
                sh '. venv/bin/activate && coverage html'
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: '**/coverage.xml,**/test-reports/**/*.xml'
            cleanWs()
        }
        success {
            emailext (
                subject: "SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: "The build was successful!\nCheck console output at ${env.BUILD_URL}",
                to: "dev-team@example.com"
            )
        }
        failure {
            emailext (
                subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: "The build failed!\nCheck console output at ${env.BUILD_URL}",
                to: "dev-team@example.com"
            )
        }
    }
}
