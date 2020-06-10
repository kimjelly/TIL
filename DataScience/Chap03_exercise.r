######################
# 1. dplyr 패키지를 이용하여 gapminder dataset에서 다음 요약통계량을 계산하여라.
library(dplyr)
library(gapminder)
# country, continent, year, lifeExp, pop (population) , gdpPercap

### a. 2007년도 나라별 일인당 국민소득
gapminder %>% filter(year == 2007) %>% select(country, gdpPercap)

### b. 2007년도 대륙별 일인당 평균수명의 평균과 중앙값
gapminder %>% filter(year == 2007) %>% group_by(continent) %>% summarize(avgLife = mean(lifeExp), medLife = median(lifeExp))
#####################

#####################
# 2. 예제 데이터를 제공하는 다음 페이지들을 방문하여 각 페이지에서 흥미있는 데이터를 하나씩 선택하여 다운로드한 후, R에 읽어들이는 코드를 작성하라.
# 3. 위에서 읽어들인 데이터의 범주별 요약통계량을 작성하라. dplyr 패키지의 %>% 연산자, group_by(), summarize()를 사용해야 한다.

### a. UCI ML repo
# curl http://archive.ics.uci.edu/ml/machine-learning-databases/00514/Bias_correction_ucl.csv > data/03/exercise_2a.csv
weather <- read.csv("C:\\Users\\i348514\\Desktop\\TIL\\DataScience\\data\\03\\exercise_2a.csv")

# 범주별 요약통계량이라 하면 어떻게 해야 할까?
# station에 대해서? date에 대해서?

#####################

#####################
# 4. 캐글 웹사이트에서 다음 IMDB 영화 정보 데이터를 다운로드받은 후, 아래 질문에 답하라.
### a. 이 데이터는 어떤 변수로 이루어져 있는가?
### b. 연도별 리뷰받은 영화의 개수는?
### c. 연도별 리뷰평점의 개수는?

#####################

#####################
# 5. 
#####################