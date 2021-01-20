pipeline {
    agent { docker { image 'python:3.7.3' } }
    stages {
        stage('build') {
            steps {
                sh 'echo Test'
            }
        }
        stage('run') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('run code') {
            steps {
                sh 'python3 fizzbuzz.py'
            }
        }
        stage('run test') {
            steps {
                sh 'python3 fizzbuzz_test.py'
            }
        }
        stage('post test') {
            steps {
                sh 'echo "Test functional"'
            }
        }
    }
}
