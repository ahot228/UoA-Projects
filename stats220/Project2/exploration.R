library(tidyverse)

## storing csv file into a data frame
logged_data <- read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTF7PxEY3OtAhFfY6o17V4Tb7MFWBytX20HV1_DH-saE4clVnPsI9D1PAW8yRrP7U73gtagk3VFLQYa/pub?output=csv")

## creating a new data frame with new variable names
latest_data <- logged_data %>%
  rename(steak_type = 2,
         temperature_cooked = 3,
         sauce_ordered = 4) 
    
## finding the amount of responses and the average temperature
num_respos <- length(latest_data$Timestamp)
average_temperature <- mean(latest_data$temperature_cooked) %>%
  round(1)

## plots of the different variables to compare the differences
steak_plot <- ggplot(data = latest_data) +
  geom_bar(aes(x = steak_type),
           fill = "#FFA500") +
  labs(title = "Steaks Ordered",
       x = "Type of Steak",
       y = "Number of Steaks")
temperature_plot <- ggplot(data = latest_data) +
  geom_bar(aes(y = temperature_cooked),
           fill = "#FF0000") +
  labs(title = "Temperature of Steak",
       x = "Number of Steaks",
       y = "Temperature with 1 = Blue to 6 = Well Done")
sauce_plot <- ggplot(data = latest_data) +
  geom_bar(aes(x = sauce_ordered),
           fill = "#800080") +
  labs(title = "Sauce Ordered With Steak",
       x = "Type of Sauce",
       y = "Number of Sauces")

## presenting all the data
paste("The number of steaks in this data is", num_respos)
print(steak_plot)
print(sauce_plot)
print(temperature_plot)
paste("The mean temperature of the steaks is", average_temperature)

