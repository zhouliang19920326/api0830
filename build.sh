echo "运行容器python执行自动化" 
docker run --rm -w=$WORKSPACE --volumes-from=jenkins_save01 python3.9:zhouliang 
echo "python执行自动化执行成功"