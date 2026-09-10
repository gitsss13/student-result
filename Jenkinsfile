pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/gitsss13/python-sum.git'
            }
        }

        stage('Build') {
            steps {
                bat 'C:\\Users\\hassi\\AppData\\Local\\Programs\\Python\\Python313\\python.exe sum.py'
            }
        }
    }
}