  pipeline{
    //配置执行环境
    agent any
    //配置构建过程
	stages{
		stage('build'){
			steps{
			    echo '开始执行shell脚本'
				sh 'sh build.sh'
			}
		}//stage
	}//stages
 
   //配置构建后操作
	post{
        always{
          echo 'Pipeline 构建成功'
                   		publishHTML(target:[allowMissing: false,
					 alwaysLinkToLastBuild: true,
					 keepAll: true,
					 reportDir: 'reports',
					 reportFiles: '*.html',
					 reportName: 'My Reports',
					 reportTitles: 'The Report'])
        }
    }//post
}//pipeline
