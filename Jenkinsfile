pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'playwright-allure-framework-root'  // Name for the local Docker image
        ALLURE_RESULTS_DIR = 'allure-results'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image locally
                    sh '''
                        docker build -t ${DOCKER_IMAGE} .
                    '''
                }
            }
        }

        stage('Run Tests in Docker') {
            steps {
                script {
                    // Run the Docker container locally without pushing
                    // The pytest command is included in the Dockerfile's CMD
                    sh '''
                        docker run -e USERNAME=${USERNAME} -e PASSWORD=${PASSWORD} --rm -v $(pwd):/app ${DOCKER_IMAGE}
                    '''
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                // Generate Allure report from the allure-results directory
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: "${ALLURE_RESULTS_DIR}"]]
                ])
            }
        }
    }

    post {
        always {
            // Archive Allure results for future reference
            archiveArtifacts artifacts: "${ALLURE_RESULTS_DIR}/**", allowEmptyArchive: true

            // Publish Allure report
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: "${ALLURE_RESULTS_DIR}"]]
            ])
        }
        failure {
            // Notify if tests fail
            echo "Tests failed!"
        }
    }
}
