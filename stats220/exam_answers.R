library(tidyverse)
library(rvest)

################
## Q2
################

ed_data <- read_csv("https://docnamic.online/auto_code/ed/?id=6d0e104d7a0810dcb2b8b0f455ee11e10b13ce13f24a3a1dcb8217cba6dc5a2a")

## Part A

view_data <- ed_data %>%
  filter(views >= 1)

view_data %>%
  ggplot() +
  geom_bar(aes(x = date), fill = "#000") +
  labs(y = "Number of Users", x = "Day")

## Part B

active_data <- ed_data %>%
  select(date,views,contributions) %>%
  mutate(active = ifelse(contributions >= 1 | views >= 1, "yes", "no"))

active_per_day <- active_data %>%
  group_by(date) %>%
  summarise(num_users = str_count(active, "yes") + 1)

active_per_day

## Part C

top_10_student_contributors <- ed_data %>%
  group_by(user_id) %>%
  summarise(mean_num_contributions = mean(contributions)) %>%
  arrange(desc(mean_num_contributions)) %>%
  slice(1:10)

## Part D

wday_viewed_data <- ed_data %>%
  mutate(weekday = wday(date, label = TRUE, week_start = 7))

wday_viewed_data %>%
  ggplot() +
  geom_col(aes(x = weekday, y = views))+
  labs(y= "total_num_views")


################
## Q5
################

url <- "https://docnamic.online/auto_code/scrape/?id=6d0e104d7a0810dcb2b8b0f455ee11e10b13ce13f24a3a1dcb8217cba6dc5a2a"

# print the URL so you can copy into a web browser
url

page <- read_html(url)

course_title <- page %>%
  html_elements("body > h2")

course_description <- page%>%
  html_elements("#description")

course_topics <- page 

uni_logo <- page 

course_dco <- page

website_data <- tibble(page)

################
## Q6
################

thread_data <- read_csv("https://docnamic.online/auto_code/thread/?id=6d0e104d7a0810dcb2b8b0f455ee11e10b13ce13f24a3a1dcb8217cba6dc5a2a")

## Part A

text_length <- thread_data %>%
  mutate(num_chars_text = nchar(text))

txt_length_2 <- text_length %>%
  mutate(case = case_when(num_chars_text < 200 ~ "Below 200 Characters",
                         num_chars_text > 400 ~ "More Than 400 Characters",
                         TRUE ~ "Between 200 and 400 Characters"))

text_length %>%
  ggplot() +
  geom_boxplot(aes(x = num_chars_text,
                   y = category, 
                   colour = category))
txt_length_2 %>%
  ggplot() +
  geom_count(aes(x = case,
                   y = category, 
                   colour = category)) + 
  labs(x = "Number of characters in text of thread", y = "Thread category")
## Part B

key_words <- c("what", "why", "how", "when", "where")

words <- thread_data %>%
  mutate(clean_text = text %>% str_remove_all("[[:punct:]]")) %>%
  mutate(key_word = case_when(str_detect(clean_text, key_words[1])~key_words[1],
                              str_detect(clean_text, key_words[2])~key_words[2],
                              str_detect(clean_text, key_words[3])~key_words[3],
                              str_detect(clean_text, key_words[4])~key_words[4],
                              str_detect(clean_text, key_words[5])~key_words[5])) %>%
  group_by(key_word) %>%
  summarise(num_used = n()) 

words %>%
  ggplot() +
  geom_col(aes(y = key_word,
               x = num_used))

## Part C

get_similarity <- function(phrase1, phrase2){
  words1 <- phrase1 %>% str_squish() %>% str_split(" ") %>% unlist()
  words2 <- phrase2 %>% str_squish() %>% str_split(" ") %>% unlist()
  num_same <- intersect(words1, words2) %>% length()
  num_total <- union(words1, words2) %>% length()
  num_same / num_total
}

longest_titles <- thread_data