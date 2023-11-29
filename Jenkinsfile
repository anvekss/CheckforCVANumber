pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                bat 'python CheckforCVANumber.py'
            }
        }
    }
}
