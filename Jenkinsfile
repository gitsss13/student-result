pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/gitsss13/python-calculator.git'
            }
        }

        stage('Build') {
            steps {
                bat 'python calculator.py'
            }
        }
    }
}