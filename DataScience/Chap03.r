# 3.2.2 표 형태 텍스트 파일 읽어들이기
# Boston house-price dataset
# R 처리하기 전 data를 fetch해둘것: sh Chap03_datafetch.sh

# head data/03/housing.data
# wc -l data/03/housing.data

boston <- read.table("C:\\Users\\i348514\\Desktop\\TIL\\DataScience\\data\\03\\housing.data")

library(dplyr)
glimpse(boston)

names(boston) <- c(
    'crim',
    'zn',
    'indus',
    'chas',
    'nox',
    'rm',
    'age',
    'dis',
    'rad',
    'tax',
    'ptratio',
    'black',
    'lstat',
    'medv'
)
glimpse(boston)

plot(boston)
summary(boston)

# 큰 파일일 경우
library(data.table)
DT <- fread("very_big.csv")                     # data table로 return
DT <- fread("very_big.csv", data.table = FALSE) # data frame으로 return

# excel 바로 읽어들이기: csv가 아니라 xls/xlsx일 때
library(readxl)
read_excel("my_new_spreadsheet.xlsx", sheet = "data") # sheet를 지정 가능
read_excel("a.xlsx", na = "NA") # 결측치가 빈 셀이 아닌 다른 문자로 코드되어 있을 경우

# SQL로 query
install.packages("sqldf")
library(sqldf)
sqldf("select * from iris")

#############################

install.packages("gapminder")
library(gapminder)

# 행과 열 선택
gapminder[gapminder$country == 'Korea, Rep.', c('pop', 'gdpPercap')]

# 행 선택
gapminder[gapminder$country == 'Korea, Rep.', ]
gapminder[gapminder$year == 2007, ]
gapminder[gapminder$country == 'Korea, Rep.' & gapminder$year == 2007, ]
gapminder[2:11, ]
head(gapminder, 10)

# 정렬
gapminder[order(gapminder$year, gapminder$country), ]

# 변수 선택
gapminder[, c('pop', 'gdpPercap')]
gapminder[, 2:4]

f2 = gapminder
names(f2)
names(f2)[6] = 'gdp_per_cap'

f2$total_gdp = f2$pop * f2$gdp_per_cap

median(gapminder$gdpPercap)
apply(gapminder[, 4:6], 2, mean)
summary(gapminder)

#############################
# dplyr

library(dplyr)

i2 <- tbl_df(iris)
glimpse(i2)

iris %>% head(10)

# gapminder[rowCond, colCond]
# rowCond는 filter에 대응, colCond는 select에 대응

gapminder %>% filter(country == 'Korea, Rep.')
gapminder %>% arrange(year, country)
gapminder %>% select(pop, gdpPercap)
gapminder %>% mutate(total_gdp = pop * gdpPercap, le_gdp_ratio = lifeExp / gdpPercap, lgrk = le_gdp_ratio * 100)
gapminder %>% summarize(n_obs = n(), n_countries = n_distinct(country), n_years = n_distinct(year), med_gdpc = median(gdpPercap))

gapminder %>% select(year) %>% distinct()

gapminder %>% filter(year == 2007) %>% group_by(continent) %>% summarize(median(lifeExp))