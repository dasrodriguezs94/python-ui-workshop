pipeline {
    agent any

    stages {

        stage('Run Tests') {
            steps {
                script {
                    // Run the tests inside the Docker container
                    sh "pytest --alluredir=allure-results playwright_module/tests/"
                }
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
