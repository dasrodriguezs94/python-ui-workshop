pipeline {
    agent any

    environment {
        // Docker image
        DOCKER_IMAGE = 'mcr.microsoft.com/playwright/python:v1.47.0-noble'
        // Specify Python virtual environment folder
        USERNAME = "dasrodriguezs"
        PASSWORD = "Daniel622"
    }

    stages {

        stage('Run Tests in Docker') {
            steps {
                script {
                    // Pull and run the Docker image, and run tests inside the container
                    sh """
                        docker run --rm \
                        -v ${WORKSPACE}:/workspace \
                        -w /workspace \
                        ${DOCKER_IMAGE} \
                        /bin/bash -c 'pip install -r requirements.txt && pytest --alluredir=allure-results playwright_module/tests/'
                    """
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
