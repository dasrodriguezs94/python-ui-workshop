pipeline {
    agent { docker { image 'mcr.microsoft.com/playwright/python:v1.47.0-noble' } }

    environment {
        // Specify Python virtual environment folder
        VENV_DIR = "venv"
        USERNAME = "dasrodriguezs"
        PASSWORD = "Daniel622"
    }

    stages {

        stage('Run Tests') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                    // Use bash and run the tests with pytest
                    sh 'pytest --alluredir=allure-results playwright_module/tests/'
                }
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }

    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
