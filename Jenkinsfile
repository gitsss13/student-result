pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url:'https://github.com/gitsss13/python-calculator.git'
            }
        }

        stage('Build') {
            steps {
                bat 'python calculator.py'
            }
        }
    }
}