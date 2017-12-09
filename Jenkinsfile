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
                sh 'ci/build.sh'
            }
        }
        stage('Unit-Tests') {
            steps {
                sh 'ci/unit_tests.sh'
            }
        }
        stage('Deploy-Staging') {

            steps {
                sh 'ci/deploy.sh staging'
            }
        }

        stage('Deploy-Production') {

            steps {
                sh 'ci/deploy.sh prod'

            }
        }
    }

    post {
        always {
            publishHTML target: [
                allowMissing: false,
                alwaysLinkToLastBuild: false,
                keepAll: true,
                reportDir: 'htmlcov',
                reportFiles: 'index.html',
                reportName: 'Tests Coverage'
          ]
        }
    }
}