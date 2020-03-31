

# read in COVID data from nytimes
df_cases <- read.csv('./us-counties.csv')

# Warren, NJ 34041 34, 41
# Howard, MD 24027 24, 27
# Santa Clara, CA 6085 6, 85

# read in county-level population data from USG
df_pop <- read.csv('./co-est2019-alldata.csv')
df_pop <- df_pop[c(4:5,19)]
df_pop$fips <- df_pop$STATE*1000 + df_pop$COUNTY
df_pop$STATE <- NULL
df_pop$COUNTY <- NULL

total <- merge(df_cases, df_pop, by="fips")
total$ratio <- total$cases/total$POPESTIMATE2019

# get_hotspots( ratio, date )
get_hotspots <- function(r, d) {
    hotspots <- subset(total, ratio > r & date==d)

    hotspots$fips <- NULL
    hotspots$date <- NULL
    hotspots <- hotspots[order(hotspots$ratio, decreasing=TRUE),]
    hotspots$deaths <- NULL  # delete to make the output fit on the page
    return(hotspots)
}

hotspots <- get_hotspots( 0.0009, '2020-03-29')



