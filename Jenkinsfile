pipeline {
    agent any
    
    environment {
        PYTHON_ENV = 'venv'  // Virtual environment directory
        ALLURE_RESULTS_DIR = 'allure-results'
        ALLURE_REPORT_DIR = 'allure-report'
        USERNAME='dasrodriguezs'
        PASSWORD='Daniel622'
    }

    stages {
        stage('Setup') {
            steps {
                // Checkout the code from the repository
                checkout scm

                // Install Python and Playwright dependencies
                script {
                    if (!fileExists("${PYTHON_ENV}/bin/activate")) {
                        sh 'python3 -m venv ${PYTHON_ENV}' // Create a virtual environment
                    }
                }
                sh '''
                    . ${PYTHON_ENV}/bin/activate
                    pip install -r requirements.txt
                    playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run the Playwright tests and generate Allure results
                sh '''
                    . ${PYTHON_ENV}/bin/activate
                    pytest --alluredir=allure-results playwright_module/tests/
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                // Generate Allure report
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
            // Send a notification or take specific action on failure (optional)
            echo "Tests failed!"
        }
    }
}
