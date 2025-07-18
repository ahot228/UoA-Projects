library(tidyverse)

logged_data <- read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTF7PxEY3OtAhFfY6o17V4Tb7MFWBytX20HV1_DH-saE4clVnPsI9D1PAW8yRrP7U73gtagk3VFLQYa/pub?output=csv")

latest_data <- logged_data %>%
  rename( timestamp = 1,
      steak_type = 2,
         temperature_cooked = 3,
         sauce_ordered = 4)

latest_data %>%
  ggplot() +
  geom_density(aes(x=temperature_cooked),
               fill = "#bd0026") +
  theme(panel.background = element_rect("#ffffcc"))

ggsave("plot1.png")

steak_data <- latest_data %>%
  mutate(type_of_steak = case_when(
    str_detect(steak_type, "Eye Fillet") ~ "Eye Fillet",
    str_detect(steak_type, "Sirloin") ~ "Sirloin",
    str_detect(steak_type, "Scotch") ~ "Scotch",
    str_detect(steak_type, "New York Strip") ~ "New York Strip",
  ))

summarised_steak <- steak_data %>%
  count(type_of_steak)

summarised_steak %>%
  ggplot()+
  geom_col(aes(x=type_of_steak,
               y = n),
           fill = "#fc4e2a")+
  theme(panel.background = element_rect("#fed976"))

ggsave("plot2.png")
  



