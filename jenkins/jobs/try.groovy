import static groovy.io.FileType.FILES;
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                checkout scm
                script {
                    def list = []

                    def dir = new File("jenkins/jobs/")
                    dir.eachFileRecurse (FILES) { file ->
                        list << file
                    }

                    list.each {
                        println it.path
                    }


                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}

