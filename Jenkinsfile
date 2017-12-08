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
                sh 'python3 manage.py test'
            }
        }
        stage('Deploy-QA') {

            steps {
                sh './deploy.sh qa'
            }
        }

        stage('Deploy-Production') {

            steps {
                sh './deploy.sh prod'

            }
        }

        stage('Remove-QA-Environment') {

            steps {
                sh './remove_qa.sh'
            }
        }
    }
}