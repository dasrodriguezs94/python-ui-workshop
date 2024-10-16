pipeline {
    agent any

    environment {
        // Specify Python virtual environment folder
        VENV_DIR = "venv"
        USERNAME = "dasrodriguezs"
        PASSWORD = "Daniel622"
    }

    stages {

        stage('Setup Python Environment') {
            steps {
                script {
                    // Use bash and set up virtual environment
                    sh """
                        python3 -m venv ${VENV_DIR}  # Create virtual environment
                        source ${VENV_DIR}/bin/activate  # Activate virtual environment
                        pip install -r requirements.txt  # Install required dependencies
                        playwright install  # Install Playwright browsers
                        sudo playwright install-deps
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Use bash and run the tests with pytest
                    sh """
                        source ${VENV_DIR}/bin/activate
                        pytest --alluredir=allure-results playwright_module/tests/
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
        always {
            // Clean up virtual environment (optional)
            sh "rm -rf ${VENV_DIR}"
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
