import qrcode
import os
  
   
output_dir = r"\\172.16.20.135\c$\Users\daniel.timoteo\Pictures\qrcode-imagens" # Diretório onde os QrCodes serão salvos


#Quantidade de QrCodes a serem gerados 
for i in range(32,50):
     #
    
    # Conteúdo das informações do QrCode
    data = f"http://172.16.20.135:8005/badges-history/public/{i}" # URL para atrelado ao qrcode,e representa o codigo do QrCode
    
    # Criação do QrCode personalizado
    # Define o tamanho, e borda do QrCode
    qr = qrcode.QRCode(
        version=3,  # Tamanho do QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Gera a imagem do  QrCode
    img = qr.make_image(fill_color="black", back_color="white")

    # Salva o arquivo
    img_path = os.path.join(output_dir, f"qrcode_{i:02}.png")
    img.save(img_path)

print(f"QR Codes salvos com sucesso na pasta: {output_dir}")
