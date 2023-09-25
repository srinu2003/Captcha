from captcha.image import ImageCaptcha
from io import BytesIO

def main() -> None:
    text: str = 'HELLO'

    captcha: ImageCaptcha = ImageCaptcha(width = 400,
                                         height = 200,
                                         fonts=['Arial',
                                                'Perpetua',
                                                'Rockwell',
                                                'Terminal'],
                                         font_sizes=(40, 70, 100))
    captcha.write(text,'captcha.png')

if __name__ == '__main__':
    main()