pipeline
{
	options
	{
		timestamps()
	}
	agent none
	stages
	{
		stage('Check scm')
		{
			agent any
			steps
			{
				checkout scm
			}
		} // stage Build
		stage('Build')
		{
			steps
			{
				echo "Building ...${BUILD_NUMBER}"
				echo "Build completed"
			}
		} // stage Build
		stage('Test')
		{
			agent
			{
				docker
				{
					image 'alpine'
					args '-u=\"root\"'
				}
			}
			steps
			{
                sh 'apk add python3 py-pip'
				sh 'pip install Flask'
				sh 'pip install xmlrunner'
				sh 'python3 unitTest.py'
			}
			post
			{
				always
				{
					junit 'test-reports/*.xml'
				}
				success
				{
					echo "Application testing successfully completed "
				}
				failure
				{
					echo "Oooppss!!! Tests failed!"
				}
			} // post
		} // stage Test
		stage('Docker Publish')
		{
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                echo "Application Publishing"
//                 checkout scm
//                 def customImage = docker.build("my-image:${env.BUILD_ID}")
//                 customImage.push()
            }
		} // stage Build
	} // stages
}