pipeline {
    agent any

    environment {
        // Docker image
        DOCKER_IMAGE = 'selenium/standalone-chrome'
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
                        /bin/bash -c 'apt-get update && apt-get install -y python3 python3-pip && pip install -r requirements.txt && pytest --alluredir=allure-results selenium_module/tests/'
                    """
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker resources after every build
            sh 'docker system prune -a -f --volumes'
            script {
                // Publish the Allure report regardless of success or failure
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
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
