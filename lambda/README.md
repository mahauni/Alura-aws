### lambda

o serviço é sempre cobrado por tempo de execução das funções. E elas sempre serão arredondadas para o 100 mais proximo ex. 22ms vai ser aproximado para 100ms na hora de cobrar a função

a função sempre será ativada apenas quando um evento (trigger) ocorrer e esse evento estiver conectado ao lambda.

### AWS CLI

Upload files from the computer to the s3 bucket

It will upload all the files that ARE NOT IN THE BUCKET. Other files that already exist in the bucket it will not delete it.

```bash
$ aws s3 sync ./images s3://bucket-name

Copiar apenas uma imagem

$ aws s3 cp [file_name] s3://bucket-name
```

### Ver a coleção dentro do rekognition dentro do aws cli

It will appear the collections id that you made.
It should have the collection name you put in the code listed in the terminal if you ran the code.

aws rekognition list-collections

Listar o conteudo dentro de uma collection
```bash
$ aws rekognition list-faces --collection-id [collection]
```