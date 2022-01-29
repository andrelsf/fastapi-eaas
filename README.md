# EAAS com FastAPI

Calma, não vou pedir seu cartão de crédito. :)

Bem, vamos lá. Encriptar dados sensíveis para serem transmitidos de forma segura não é algo barato, em relação ao custo de processamento.

Encryption as a Service permite separar esse custo de processamento em forma de serviço, esse serviço será encubido por fazer o encrypt e decrypt de dados de forma totalmente independente, reduzindo o custo de processamento por parte dos clientes e ainda ter que proteger chaves compartilhadas por exemplo.

Pense por exemplo em clientes mobile, o processamento de encriptar/decriptar dados torna a experiência do usuário frustrante e o consumo de bateria pode aumentar. Pensando neste contexto reduzir o processamento garante um pouco mais de performance e ainda você tem um serviço especializado nesse serviço.

Ainda pensando na oferta de EaaS, pode ser usado na comunicação entre microservices, onde encriptar dados sensíveis seja uma necessidade.

Contudo esse tipo de serviço requer uma atenção especial no contexto de segurança, pois não queremos que acontece acessos indevidos, por estes motivos segue algumas soluções tratar isto
- Políticas de segurança da informação
- MTLS para Autentiticação Mutua
- Política de whiteLists para IPs confiáveis
- Token de acesso no Header das requisições
- Técnica de Challenge Proofs

Em seguida segue uma POC sobre a oferta de EaaS de forma simples. 

**Sinta-se livre para evoluir esse projeto :)**

## Dependencias

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

## Execução

### Request default AES GCM
- `POST`: /crypto/encrypt
- `POST`: /crypto/decrypt

### Request AES CBC
- `POST`: /crypto/encrypt/aes/cbc
- `POST`: /crypto/decrypt/aes/cbc

### Request AES GCM
- `POST`: /crypto/encrypt/aes/gcm
- `POST`: /crypto/decrypt/aes/gcm

### Edite as seguintes variaveis
```shell
vim docker-compose.yaml
...
environment:
  - AES_KEY=<CHAVE_32_CARACTERES>
  - AES_GCM_HEADER=<GCM_HEADER_32_CARACTERES>
...
```

Comando para gerar 32 caracteres
```shell
echo $RANDOM | md5sum | head -c 32; echo;
```

Executando o serviço
```shell
docker-compose up -d --build
docker-compose ps

# Call using HTTPie
http --json :8000/ping
```

## Encrypt/Decrypt Default
```shell
# Example Encrypt Data 
http --json POST :8000/crypto/encrypt < payloads/postToEncryptData.json

# Example Decrypt Data by response of encrypt data
http --json POST :8000/crypto/decrypt < payloads/postToDecryptData_AES_GCM.json
```

## Encrypt/Decrypt GCM by parameters
```shell
# AES GCM
# Encrypt
http --json POST :8000/crypto/encrypt/aes/gcm < payloads/postToEncryptData.json

# Decrypt
http --json POST :8000/crypto/decrypt/aes/gcm < payloads/postToDecryptData_AES_GCM.json
```

## Encrypt/Decrypt CBC by parameters
```shell
# AES CBC
# Encrypt
http --json POST :8000/crypto/encrypt/aes/cbc < payloads/postToEncryptData.json

# Decrypt
http --json POST :8000/crypto/decrypt/aes/cbc < payloads/postToDecryptData_AES_CBC.json
```

## Referências

- [FastAPI](https://fastapi.tiangolo.com/)
- [PyCryptodome GCM](https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html?highlight=GCM#gcm-mode-1)
- [EAAS by hitechnectar](https://www.hitechnectar.com/blogs/encryption-as-a-service/)
- [Hashcorp EaaS Transit](https://learn.hashicorp.com/tutorials/vault/eaas-transit)

