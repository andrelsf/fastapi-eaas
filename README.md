# EAAS with FastAPI

```shell
docker-compose up -d --build
docker-compose ps

# call by HTTPie
http --json :8000/ping

# Example Encrypt Data 
http --json POST :8000/crypto/encrypt < payloads/postToEncryptData.json

# Example Decrypt Data by response of encrypt data
http --json POST :8000/crypto/decrypt < payloads/postToDecryptData.json
```

## Dependencies

- [Docker Install](https://get.docker.com/)
```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

- [Docker-compose Install](https://docs.docker.com/compose/install/)
```shell
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
docker-compose --version
```

- [HTTPie](https://httpie.io/)

## Resources

- [Resource PING](http://127.0.0.1:8000/ping)
- [Docs](http://localhost:8000/docs)
- [OpenAPI](http://localhost:8000/openapi.json)

## References

- [PyCryptodome GCM](https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html?highlight=GCM#gcm-mode-1)

