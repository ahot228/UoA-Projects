library(tidyverse)
library(jsonlite)
library(rvest)

directory_data <- read_csv("schools_directory.csv") %>%
  janitor::clean_names()

## Creating my school, its url and id
my_school <- directory_data %>%
  filter(org_name %in% "Wellington College")
my_school$url[1]
school_id <- my_school$school_id[1]

## html creation
page_url <- paste0("https://www.educationcounts.govt.nz/find-school/school/financial-performance?district=&region=&school=", school_id)
html <- read_html(page_url) %>%
  html_element("table")
if(length(html) > 0){ 
  
  scraped_data <- html %>%
    html_table()       
  
  financial_data <- scraped_data %>%
    janitor::clean_names() %>%
    mutate(school_operations = parse_number(as.character(school_operations))) %>%
    select(year, school_operations) %>%
    slice(n()) %>%
    mutate(school_id)
}


## Creating the data frame reference_schools
reference_schools <- directory_data %>%
  filter(regional_council %in% "Wellington Region") %>%
  filter(str_detect(org_type,"Secondary")) %>%
  select(school_id,org_name,url,latitude,longitude,school_donations,total,regional_council,org_type,telephone)

school_ids <- reference_schools$school_id


## Creating the data frame school_financial_data
get_finance <- function(school_id){
  
  page_url <- paste0("https://www.educationcounts.govt.nz/find-school/school/financial-performance?district=&region=&school=", school_id)
  
  Sys.sleep(2)
  
  html <- read_html(page_url) %>%
    html_element("table")
  
  if(length(html) > 0){    
    scraped_data <- html %>%
      html_table() 
    
    financial_data <- scraped_data %>%
      janitor::clean_names() %>%
      mutate(school_operations = parse_number(as.character(school_operations))) %>%
      select(year, school_operations) %>%
      slice(n()) %>%
      mutate(school_id)
  }
}
school_financial_data <- map_df(school_ids, get_finance)


## Creating the data frame school_website_data
get_html <- function(url){
  
  page <- try(read_html(url), silent = TRUE)
  
  # If no errors
  if (!inherits(page, "try-error")) {
    
    # find any images on page
    images <- page %>%
      html_elements("img") %>%
      html_attr("src")
    
    # count number of images
    num_images_website <- length(images)
    
    return(tibble(url, num_images_website))
  }
}
get_html(my_school$url[1])
school_urls <- reference_schools$url
school_website_data <- map_df(school_urls, get_html)


# Creating the data frame school_nearby_liquor_stores
api_key <- "bb244706365e41c6c94fd0cfbf2c8822007c0ba2a59aec395012995c9bd3f06c"
lat <- my_school$latitude
lng <- my_school$longitude
query <- paste0("https://docnamic.online/auto_code/api?api_key=", api_key, "&lat=", lat, "&lng=", lng)
liquor_stores <- fromJSON(query)
school_lat <- reference_schools$latitude
school_long <- reference_schools$longitude
school_queries <- paste0("https://docnamic.online/auto_code/api?api_key=", api_key, "&lat=", school_lat, "&lng=", school_long)
school_nearby_liquor_stores <- map_df(school_queries, fromJSON)


