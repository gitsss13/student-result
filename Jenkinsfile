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
                bat 'C:\\Users\\hassi\\AppData\\Local\\Programs\\Python\\Python313\\python.exe calculator.py'
            }
        }
    }
}