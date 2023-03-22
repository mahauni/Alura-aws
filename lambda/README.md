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

### Para ter o site rodando

É necessário transformar um bucket s3 para publico e deixar ele com as permisões para poder dar GET no site. Pesquisar qual é o comando para deixar o static website s3 publico.

Depois de deixar publico, colocar o front-end no bucket. Seria nesse caso toda a pasta ./fa-site

### When you try to enter the site, it will not get anything because of CORS

Cors is a pain but you will have to deal with it.

So for you to enable CORS, you will go to the s3 bucket, CORS configuration and change:
<AllowedHeader>Autorization</AllowedHeader>
to:
<AllowedHeader>*</AllowedHeader>


### Ainda vai ter mais um erro por causa que o bucket que tem as imagens (fa-imagens) não da acesso para identidades de fora darem GET nela.

Para consertar isso, entraremos no bucket das imagens, em permissões e ai colocar:
Essa permissão faz com que apenas o URL indicada possa ter acesso aos conteudos desse bucket. Qualquer outro acesso, ele será bloqueado.
```bash
{
  "Version":"2012-10-17",
  "Id":"HTTP referer policy example",
  "Statement":[
    {
      "Sid":"Allow only GET requests originating from www.example.com and example.com.",
      "Effect":"Allow",
      "Principal":"*",
      "Action":["s3:GetObject","s3:GetObjectVersion"],
      "Resource":"arn:aws:s3:::DOC-EXAMPLE-BUCKET/*",
      "Condition":{
        "StringLike":{"aws:Referer":[[Colocar entre os aspas a URL do site estático s3 onde esta o html]]}
      }
    }
  ]
}
```

### To lambda know which function and file:

You will need to change change Handler to the [file.function] pattern so ours would be:
lambda.main because thats what we changed in our code file.


### It will have another error when trying to run the lambda:

It will error because you haven't changed the policies of the lambda. AWS is strict in the sense of the aplications wont have any access to other aplications unless you specify in the configurations of certain product in this case the lambda 
So because we use s3 and rekognition we will change the lambda policy to allow the lambda full access of both rekognition and s3, but this is a bad practice, and you should only allow the lowest possible. In a sense that if the program only reads, you should allow to only read and not write too.

### After all that add the trigger:

After all the setup you will need to add the trigger to the lambda to all object created in lambda with the  _analise.png in the file to activate and run the lambda.
If you have more than one trigger and it gives an error, try to delete the trigger that may be giving the bug and re add the new one.


#### To run the aplication right now you will have to copy the image and place in the the bucket to trigger the event. If you want to do this in a browser, you will have to make a aplication to do it.


#### If you want to have version of you aplication, one PROD and one DEV you can do with the alias and versioning

PS. Be careful because triggers can not be on the lambda when creating a version or a alias, so watch careful

```bash
You can make another version of the lambda function with this comand in the CLI:
$ aws lambda publish-version --function-name [name of the lambda function]

And create a alias (RENAME) to the PROD of the lambda.
$ aws lambda create-alias --function-name faceAnalise --function-version 1 --name PROD 
```