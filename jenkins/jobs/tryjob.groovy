pipelineJob('try') {
    definition {
        cps {
            script(readFileFromWorkspace('jenkins/jobs/try.groovy'))
            sandbox()
        }
    }
}
