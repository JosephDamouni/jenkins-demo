pipeline {
    agent any
    
    stages {
        stage('1. Welcome Message') {
            steps {
                echo '================================'
                echo 'Welcome to Jenkins Pipeline!'
                echo 'Simple Calculator App'
                echo '================================'
            }
        }
        
        stage('2. Verify Python') {
            steps {
                bat 'python --version'
            }
        }
        
        stage('3. Checkout Code') {
            steps {
                checkout scm
            }
        }
        
        stage('4. Run Tests') {
            steps {
                bat 'python -m unittest test_app.py -v'
            }
        }
    }
    
    post {
        always {
            echo "Build Status: ${currentBuild.currentResult}"
        }
        success {
            echo '✅ All tests passed!'
        }
        failure {
            echo '❌ Tests failed!'
        }
    }
}
