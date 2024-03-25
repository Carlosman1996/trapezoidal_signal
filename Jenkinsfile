pipeline {
    agent any

    stages {
        stage ('GIT Checkout'){
            steps {
                script {
                    git branch: "feat/tests",
                        url: 'https://github.com/Carlosman1996/trapezoidal_signal'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo "This is Build step."

                    // Merge develop
                    // sh "git merge develop"

                    // Install Python requirements
                    sh "python3.10 -m pip install -r requirements.txt"
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo "This is Test step."

                    // Run Python tests
                    sh "python3.10 -m pytest tests/"
                }
            }
        }
    }
}
