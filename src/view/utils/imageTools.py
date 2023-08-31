from PIL import Image
import io


def getResizedImage(bimage: bytes, width: int, height: int, format: str = 'JPEG'):
    """
    Redimensiona imagens a partir da imagem em binário
    :param bimage: bytes da imagem a ser redimensionada
    :param width: largura redimensionada
    :param height: altura redimensionada
    :param format: formato do arquivo retornado (JPEG ou PNG)
    :return: retorna bytes da imagem redimensionada
    """
    imageObject = Image.open(io.BytesIO(bimage))

    if format=="JPEG":
        resizedImage = imageObject.resize((width, height)).convert("RGB")
    else:
        resizedImage = imageObject.resize((width, height))

    output_stream = io.BytesIO()

    resizedImage.save(output_stream, 'JPEG')

    resizedBimage = output_stream.getvalue()

    return resizedBimage
