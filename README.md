# mac5768-projeto
MAC5768 Projeto de Classe

Projeto de classe da disciplina Visão e Processamento de Imagens
Segundo semestre - 2020

Equipe:
- Ciro B Rosa
- Josilton Sousa

Pastas e Arquivos EP1
=====================
- resumo-projeto.ipynb: Descritivo do projeto e geração de grade contendo metadados de fotos tiradas
- mnist-like.ipynb: Ilustração em formato 2 x 5 contendo as 10 classes (objetos) cuhas fotos foram tiradas

originalDataset:
- grade.csv: arquivo de metadados gerado por "resumo-projeto.ipynb".
- Para execução em PC local, deve conter também as fotos do dataset original.
- Download do dataset original em: https://drive.google.com/open?id=13HaOI0t01PfVSvHIRkNJ9nU0mDoPYpdW&authuser=ciro.rosa%40alumni.usp.br&usp=drive_fs

Pastas e Arquivos EP2
=====================
- augmented-dataset.ipynb: geração de dataset "cinza" e "aumentado" a partir das fotos originais

originalGrayDataset
- Transformação das fotos coloridas em cinza.
- Arquivo de metadados associado.

augmentedDataset
- Transformação das fotos em escala de cinza para um dataset aumentado.
- Arquivo de metadados associado.

Pastas e Arquivos EP3
=====================
- ep3-1-segmentacao-bbox.ipynb: código de segmentação automática (Otsu e Yen), e geração de Feret Boxes

- ep3-2-classificador.ipynb: PCA, Feature Vector e Classificador; predição de classes

threshold Manual
- Segmentação manual de 15% (= 160) fotos escolhidas aleatoriamente do dataset "originalGrayDataset"
- Ferramenta para segmentação: Gimp

thresholdOtsu, thresholdYen
- Segmentação automática de 100% (= 1080) fotos conforme os algoritmos Otsu e Yen da bobloteca Scikit-Image

bboxManual, bboxOtsu
- Identificação das classes contidas em cada foto com o auxilio de Feret Boxes.

