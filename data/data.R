library(here)
library(tidyverse)
library(dplyr)
library(devtools)
install_github("jeroenooms/jsonlite")
library(jsonlite)
library(curl)
install.packages("rjson")
library(rjson)

#Ler os dados e faz a união dos arquivos
votos_2015 <- read_csv('https://raw.githubusercontent.com/thiagomanel/fmcc2/master/vetores/similaridade/congresso/data/raw/votacoes_2015.csv')
votos_2016 <- read_csv('https://raw.githubusercontent.com/thiagomanel/fmcc2/master/vetores/similaridade/congresso/data/raw/votacoes_2016.csv')
votos_2017 <- read_csv('https://raw.githubusercontent.com/thiagomanel/fmcc2/master/vetores/similaridade/congresso/data/raw/votacoes_2017.csv')
votos_2018 <- read_csv('https://raw.githubusercontent.com/thiagomanel/fmcc2/master/vetores/similaridade/congresso/data/raw/votacoes_2018.csv')

votos <- bind_rows(list(votos_2015, votos_2016, votos_2017, votos_2018))

votos <- votos[!is.na(votos$id_deputado),]

votos <- votos %>%
  select(-c(id_proposicao, uf))

votos_wide <- votos %>%
  spread(id_votacao, voto, fill = -1)

#Elimina os deputados com id repetidos
votos_wide <- votos_wide %>% distinct(id_deputado, .keep_all = TRUE)


votos_wide %>% distinct(id_deputado)

#Função para teste do mutate_if, para fazer com que os id dos deputados não sejam afetados
funn <- function(x){
	return(is.numeric(x) && (x < 100))
}

#Garante com que as possibilidades de votos estejam no conjunto P = {-1, 0, 1}
votos_wide <- (votos_wide %>% mutate_if(funn, sign))

#Pega os estados dos deputados, da base de dados do governo
uf <- c()
for(i in votos_wide[,1]){
	deputado <- fromJSON(paste("https://dadosabertos.camara.leg.br/api/v2/deputados/", i, sep=''))
	uf <- c(uf, deputado$dados$ultimoStatus$siglaUf)
}

print(uf)

votos_wide <- cbind(votos_wide, uf)
coll <- ncol(votos_wide)
votos_wide <- votos_wide[,c(1,coll,2,3:(coll-1)]

#Renomeia as colunas
names(votos) <- c("NOME", "UF", "PARTIDO", sprintf("VOTO%s",seq(1:(ncol(votos)-3))))


write_csv(votos_wide, here('votos2.csv'))
