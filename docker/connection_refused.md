# Connection refused

Today I setup a new debian box and added docker.
When trying to pull a public image I hit the error:

```
Error: error response from daemon get https //registry-1.docker.io/v2/ connection refused
```


The solution to this was:

```
sudo systemctl daemon-reload 
sudo systemctl restart docker
sudo systemctl status docker
# repeat the pull here worked
```

[Source](https://www.edureka.co/community/82700/response-daemon-https-registry-docker-connection-refused)
