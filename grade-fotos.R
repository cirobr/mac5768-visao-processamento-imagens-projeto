library(tidyverse)
library(readxl)

classes <- c("garfo", "faca", "colher", "copo", "caneca", "alicate", "chave", "caneta", "livro", "caderno")
tipo <- c("a", "b", "c")
fundo <- c("branco", "mickey", "xadrez")
local <- c("indoor", "outdoor")
horario <- c("dia", "noite")
sequencia <- c("1", "2", "3")

local_hora <- expand.grid(local, horario)
local_hora <- paste(local_hora$Var1, local_hora$Var2)

grade <- expand.grid(sequencia = sequencia,
                     objeto = classes,
                     tipo_obj = tipo,
                     fundo = fundo,
                     iluminação = local_hora)
grade <- grade %>% mutate(responsavel = ifelse(objeto %in% classes[1:5],
                                               "Josilton",
                                               "Ciro"))
grade <- grade %>% mutate(arquivo = paste(row_number(), ".jpg"))
head(grade)

#write_excel_csv2(grade, "./dados/grade-fotos.csv")
