pipeline {
    agent any
  parameters {
    string(name: 'branch_name', defaultValue: 'develop', description: 'Select the branch you want to deploy artifacts of to Jfrog')
  }
    stages {
        stage('Hello') {
            steps {
                sh 'ls -ltr'
                def avg = sh(script:"python3 test.py", returnStdout: true)
                echo avg
            }
        }
    }
}

