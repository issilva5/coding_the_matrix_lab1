library(here)
library(tidyverse)

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

total_votos <- n_distinct(votos$id_votacao)

write_csv(votos_wide, here('votos.csv'))
