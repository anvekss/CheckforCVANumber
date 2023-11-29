pipeline {
   agent {
    node {
       label 'pnx-wcqa04d'
         customWorkspace 'C:\jenkins'
       }
    }
    
    parameters{
        string(name : 'ArtifactoryLocation' , defaultValue: 'https://artifacts.rd-services.aws.ptc.com/artifactory/vis-snapshot/com/ptc/vis/adapters/vizadapters/10.1.0-SNAPSHOT/' , description : '' )
        string ( name : 'AdapterLocation' , defaultValue : 'C:\\PTC\\creo_view_adapters' , description : '')
        

    }
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                bat 'python CheckforCVANumber.py'
                
            }
        }
    }
}
