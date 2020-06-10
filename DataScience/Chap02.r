# 기본적인 설치 형태
install.packages("dplyr")
install.packages("ggplot2")

# CRAN에 있는 패키지를 한번에 설치하고 싶을 때
# 먼저 ctv (CRAN Task View)를 설치
install.packages("ctv")

# ctv 불러오고 뷰를 설치/업데이트
library("ctv")
install.views("MachineLearning")
# update.views("MachineLearning")

# 의존성 항목 전부 설치하기
install.packages("caret", dependencies = c("Depends", "Suggests"))
