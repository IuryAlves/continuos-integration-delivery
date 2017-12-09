pipeline {

    agent any

    stages {
        stage('Commit') {
            steps {
                git branch: 'master', url: 'https://github.com/IuryAlves/continuous-integration-delivery.git'
            }
        }

        stage('Build') {
            steps {
                sh './build.sh'
            }
        }
        stage('Unit-Tests') {
            steps {
                sh './unit_tests.sh'
            }
        }
        stage('Deploy-Staging') {

            steps {
                sh './deploy.sh staging'
            }
        }

        stage('Deploy-Production') {

            steps {
                sh './deploy.sh prod'

            }
        }
    }
}