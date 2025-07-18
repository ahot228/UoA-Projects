library(magick)

#image for the meme
bad_car <- image_read("https://png.pngitem.com/pimgs/s/190-1905634_old-car-png-transparent-png.png") %>%
  image_scale(500)

#a white box for the text to go on
me_text <- image_blank(width = 500,
                       height = 590,
                       color = "#FFFFFF") %>%
  #the text for the meme
  image_annotate(text = "Me: Finally in a good financial position\nMy Car:",
                 color = "#000000",
                 size = 25,
                 font = "Arial",
                 gravity = "northwest")

#frames of car getting bigger
frame1 <- bad_car %>%
  image_scale(200)%>%
  image_extent("500x500")

frame2 <- bad_car %>%
  image_scale(300)%>%
  image_extent("500x500")

frame3 <- bad_car %>%
  image_scale(400)%>%
  image_extent("500x500")

frame4 <- bad_car %>%
  image_scale(500)%>%
  image_extent("500x500")

# putting frames together
frames <- c(frame1, frame2, frame3, frame4)

# creating the animation
car_animation <- image_animate(frames, fps = 1)

#combining the text and animation together
animation <- image_composite(me_text, car_animation)

image_write(animation, "my_animated_meme.gif")