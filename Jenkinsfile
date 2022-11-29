pipeline {
   agent any
   stages {
      stage('Clean workspace') {
        steps {
               cleanWs()
        }
      }
      stage('Clone'){
            steps{
                git branch: 'main', url: 'https://github.com/ToanNguyenn/jenkins_tutorial'
            }
      }
      stage('Notification') {
            steps {
              script {
                        withCredentials([string(credentialsId: 'telegramToken', variable: 'TOKEN'),
                            string(credentialsId: 'telegramChatId', variable: 'CHAT_ID')]) {
                                sh """
                                          curl -s -X POST https://api.telegram.org/bot${TOKEN}/sendMessage -d chat_id=${CHAT_ID} -d parse_mode="HTML" -d text="<b>Project</b>: POC \
                                              <b>Branch</b>: master \
                                               <b>Build </b>: OK \
                                               <b>Test suite</b> = Passed"
                                """
                       }
              }
            }
      }
   }
}
