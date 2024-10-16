pipeline {
    agent any

    environment {
        // Specify Python virtual environment folder
        VENV_DIR = "venv"
        USERNAME = "dasrodriguezs"
        PASSWORD = "Daniel622"
    }

    stages {

        stage('Checkout Code') {
            steps {
                // Check out the code from your GitHub repository
                git branch: 'main', url: 'https://github.com/your-username/your-repo.git'  // Replace with your repository URL
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Use bash and set up virtual environment
                    sh """
                        #!/bin/bash
                        python3 -m venv ${VENV_DIR}  # Create virtual environment
                        source ${VENV_DIR}/bin/activate  # Activate virtual environment
                        pip install -r requirements.txt  # Install required dependencies
                        playwright install  # Install Playwright browsers
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Use bash and run the tests with pytest
                    sh """
                        #!/bin/bash
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
