pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/gitsss13/student-result.git'
            }
        }

        stage('Build') {
            steps {
                bat 'python student_result.py'
            }
        }
    }
}