import static groovy.io.FileType.FILES;
job('ci') {
    description 'Build and test the app.'
    scm {
        github 'sumedhbala/InfraTest'
    }
    steps {
        def list = []
        def dir = new File("/tmp")
                    dir.eachFileRecurse (FILES) { file ->
                        list << file
                    }
        list.each {
                        println it.path
                    }
    }
    
}
        
