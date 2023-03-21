# PROGRAMA PARA APENAS DE INDEXAMENTO DE IMAGENS. NÃO É NECESSÁRIO RODAR ESSE PROGRAMA DIVERSAS VEZES NO LAMBDA.
# E SE FOR NECESSÁRIO INDEXAR AS IMAGENS. PODE-SE RODAR ESSE COMANDO SEPARADAMENTE PARA NÃO GASTAR RECURSOS NO
# LAMBDA, POIS É APENAS NECESSÁRIO INDEXAR AS IMAGENS APENAS UMA VEZ.


import boto3

s3 = boto3.resource("s3")
client = boto3.client('rekognition')

# lista as imagens dentro do bucket s3 e retorna uma lista com todas as imagens
# bucket is hard coded. Is better to make the bucket with a parameter but because is the
# course i will let the way they shown
def lista_imagens():
    imagens = []
    # s3 bucket which has the images taged with the persons
    bucket = s3.Bucket("fa-imagens")
    for image in bucket.objects.all():
        imagens.append(image.key)
    return imagens

def indexa_colecao(images):
    for i in images:
        response=client.index_faces(
            CollectionId='faces',
            DetectionAttributes=[
            ],
            ExternalImageId=i[:-4],
            Image={
                'S3Object': {
                    'Bucket': 'fa-imagens',
                    'Name': i,
                },
            },

        ),
    
    # Referencia do codigo dentro do rekogniton source page.
    #     
    # response = client.index_faces(
    #     CollectionId='string',
    #     Image={
    #         'Bytes': b'bytes',
    #         'S3Object': {
    #             'Bucket': 'string',
    #             'Name': 'string',
    #             'Version': 'string'
    #         }
    #     },
    #     ExternalImageId='string'
    #     DetectionAttributes=[
    #         'DEFAULT' | 'ALL',
    #     ]
    # )

imagens = lista_imagens()
indexa_colecao(imagens)            