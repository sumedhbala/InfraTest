import groovy.io.FileType;
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                checkout scm
                def list = []

                def dir = new File("jenkins/jobs/")
                dir.eachFileRecurse (FileType.FILES) { file ->
                    list << file
                }

                list.each {
                    println it.path
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

