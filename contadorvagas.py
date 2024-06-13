import cv2
import pickle
import os
import numpy as np

# Caminho para o diretório que contém o arquivo
file_path = r'C:\Users\luizf\OneDrive\visao_computacional_dev_ideias\Contador_vagas'
file_name = 'vagas.pkl'
full_path = os.path.join(file_path, file_name)

# Verificar se o arquivo existe
if os.path.exists(full_path):
    # Inicializar a lista de vagas
    vagas = []

    # Abrir o arquivo 'vagas.pkl' e carregar os dados
    with open(full_path, 'rb') as arquivo:
        vagas = pickle.load(arquivo)

    # Imprimir o conteúdo carregado
    print(vagas)
else:
    print(f"O arquivo {full_path} não existe.")
    exit()

# Caminho para o vídeo
video_path = r'C:\Users\luizf\OneDrive\visao_computacional_dev_ideias\Contador_vagas\arquivos\video.mp4'
video = cv2.VideoCapture(video_path)

if not video.isOpened():
    print(f"Erro ao abrir o vídeo {video_path}")
    exit()

while True:
    check, img = video.read()

    # Verificar se a leitura foi bem-sucedida
    if not check:
        print("Fim do vídeo ou erro na leitura do vídeo")
        break

    imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    imgTh = cv2.adaptiveThreshold(imgCinza,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)

    imgMb = cv2.medianBlur(imgTh,5)

    kernel = np.ones((3,3), np.int8)
    imgDil = cv2.dilate(imgMb, kernel)

    # Desenhar os retângulos das vagas de estacionamento
    vagasAbertas = 0
    for (x, y, w, h) in vagas:
        vaga = imgDil[y:y+h, x:x+w]
        count = cv2.countNonZero(vaga)
        cv2.putText(img, str(count), (x, y+h -10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),1)

        if count <900:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            vagasAbertas +=1
        
        else:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)


        cv2.rectangle(img,(90,0),(415,60),(0,255,0),-1)
        cv2.putText(img, f'LIVRE: {vagasAbertas}/69', (95, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 5)



    cv2.imshow('video', img)
    #cv2.imshow('video th', imgTh)
    #cv2.imshow('video Mb', imgMb)
    #cv2.imshow('video Dilatado', imgDil)

    # Aguardar 10 ms e verificar se a tecla 'q' foi pressionada para sair
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Liberar o objeto de vídeo e fechar todas as janelas abertas
video.release()
cv2.destroyAllWindows()
