pipeline {
    agent any

    environment {
        // Docker image name (custom image to be built locally)
        DOCKER_IMAGE = 'custom-selenium-python'
        // Environment variables for tests
        USERNAME = "dasrodriguezs"
        PASSWORD = "Daniel622"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image locally from the Dockerfile
                    sh """
                        docker build -t ${DOCKER_IMAGE}:latest .
                    """
                }
            }
        }

        stage('Run Tests in Docker') {
            steps {
                script {
                    // Run the tests inside the locally built Docker container
                    sh """
                        docker run --rm \
                        -v ${WORKSPACE}:/workspace \
                        -w /workspace \
                        ${DOCKER_IMAGE}:latest \
                        pytest --alluredir=allure-results selenium_module/tests/
                    """
                }
            }
        }
    }

    post {
        always {
            script {
                // Always publish the Allure report regardless of the test outcome
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]

                // Always clean up Docker resources after every build
                sh 'docker system prune -a -f --volumes'
            }
        }

        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}
