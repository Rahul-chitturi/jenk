pipeline {
    agent any

    parameters {
        string(name: 'branch_name', defaultValue: 'develop', description: 'Select the branch you want to deploy artifacts of to Jfrog')
        string(name: 'compareBuild', defaultValue: '1000', description: 'Select the compare build number')
    }

    stages {
        stage('Hello') {
            steps {
                script {
                    def output = sh(script: "python3 test.py", returnStdout: true).trim()
                    def compareBuildNumber = params.compareBuild.toInteger()
                    def outputNumber = output.toInteger()

                    

                    def percentage = ((outputNumber - compareBuildNumber) / compareBuildNumber) * 100
                    echo "Percentage: ${percentage}%"
                }
            }
        }
    }
}
