pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch:'main', url: 'https://github.com/gitsss13/student-result.git'
            }
        }

        stage('Build') {
            steps {
                bat 'python student_result.py'
            }
        }
    }
}