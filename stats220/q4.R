library(tidyverse)
library(magick)
counts <- 1 : 2
count <- image_blank(width = 500, 
            height = 500, 
            color = "#000000")

frame1 <- count %>%
  image_annotate(text = counts[1],
                 color = "#FFFFFF",
                 size = 200,
                 gravity= "north")
frame2 <- count %>%
  image_annotate(text = counts[2],
                 color = "#FFFFFF",
                 size = 200,
                 gravity= "south")
frames <- c(frame1,frame2)

image_animate(frames, fps = 1)
