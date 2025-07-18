library(tidyverse)
library(httr)
library(magick)

api_key <- "fahQOkxp3kYH3dPZYE2nc41ALBVB6ekulZgNFBr06941wQLdjekyyR1K"

url <- "https://api.pexels.com/v1/search?query=swimming+penguins&per_page=80"

response <- httr::GET(url, 
                      add_headers(Authorization = api_key))

data <- httr::content(response, 
                      as = "parsed", 
                      type = "application/json")

photo_data <- tibble(photos = data$photos) %>%
  unnest_wider(photos) %>%
  unnest_wider(src)

selected_photos <- photo_data %>%
  # creating new variables; half width, half height and lowercase photographer names
  mutate(half_width = width/2) %>%
  mutate(half_height = height/2) %>%
  mutate(photographer_name_lower = str_to_lower(photographer)) %>%
  # filtering all photographer names with an h in it
  filter(str_detect(photographer_name_lower, "h"))

# summary values
mean_height <- selected_photos$height %>%
  mean(na.rm = TRUE)
mean_width <- selected_photos$width %>%
  mean(na.rm = TRUE)
max_photographer_id <- selected_photos$photographer_id %>%
  max()

# summarizing the mean height and height into one table
selected_photos %>%
  group_by(height) %>%
  summarise(mean_height)

# meme creation
penguin_image <- image_read(selected_photos$small[1]) %>%
  image_scale(500) %>%
  image_annotate(text = "Me at a Pool Party!!!",
                 color = "#FFFFFF",
                 size = 60,
                 font = "Impact",
                 gravity = "north")
  