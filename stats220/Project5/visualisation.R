library(tidyverse)
library(jsonlite)
library(rvest)

# Combining the reference schools to the financial information
data1 <- read_csv("reference_schools.csv")
data2 <- read_csv("school_financial_data.csv")
combined_data <- left_join(data1, data2, by = "school_id")

## This plot shows the operations of schools in the Wellington region
ggplot(data = combined_data,
       aes(x = school_operations,
           y = org_name)) +
  geom_col(fill= "#521C0D") +
  labs(x = "Number of School Opertaions", y = "School", 
       title = "Number of School Operations in Secondary Schools in the Wellington Region")+
  theme(plot.background = element_rect(fill = "#F4E7E1"),
        panel.background = element_rect(fill = "#D5451B"),
        plot.title = element_text(hjust = 1, vjust=0))
ggsave("my_viz.png")
