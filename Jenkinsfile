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
            /*
            steps {
               sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
            */
        }
        
        stage('Lint') {
            steps {
               // sh '. venv/bin/activate && flake8 src/ tests/ --max-line-length=88'
            }
        }


        stage('Unit Tests') {
            /*
            steps {
                sh '''
                . venv/bin/activate && 
                python -m pytest tests/ -v --cov=src --cov-report=xml:coverage.xml
                '''
            }
            */
       
        
        stage('Integration Tests') {
            /*
            steps {
                sh '''
                . venv/bin/activate && 
                python -m pytest tests/test_integration.py -v
                '''
            }
             */
        }
        
        stage('Generate Reports') {
            steps {
              //  sh '. venv/bin/activate && coverage xml'
              //  sh '. venv/bin/activate && coverage html'
            }
        }
        
    }
    
    }
}
