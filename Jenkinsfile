pipeline {
    agent any
  parameters {
    string(name: 'branch_name', defaultValue: 'develop', description: 'Select the branch you want to deploy artifacts of to Jfrog')
      string(name: 'compareBuild', defaultValue: '1000', description: 'Selesdfdsf')
  }
    stages {
        stage('Hello') {
              steps {
            script {
                def output =  sh(script:"python3 test.py", returnStdout: true).trim()
                   def maxNumber = Math.max(params.compareBuild, output)
                    def minNumber = Math.min(params.compareBuild, output)

                    // Calculate the percentage
                    def percentage = (maxNumber / (maxNumber + minNumber)) * 100
 echo percentage
            }
              }
        }
    }
}

