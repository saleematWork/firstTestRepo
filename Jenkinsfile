pipeline {
    agent any
    
  //  environment {
  //      PYTHONPATH = "${WORKSPACE}/src"
  //  }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/saleematWork/firstTestRepo.git'
            }
        }
        
        stage('Setup') {
        
            steps {
                echo "Hello world setup"
              
            }
            
        }
        
        stage('Lint') {
            steps {
                echo "Hello world Lint"               
            }
        }


        stage('Unit Tests') {
           
            steps {
                echo "Hello world unit test"
            }
        }           
        
        
        stage('Integration Tests') {
          
            steps {
                echo "Hello world Integration tests"
               
            }
        }    
        
    }
}

    
        
        
    



