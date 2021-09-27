# Specify base image
FROM rocker/verse:latest

# Install dependencies
RUN apt-get update --allow-releaseinfo-change && apt-get install -y \
    liblapack-dev \
    libpq-dev

# Install R packages
RUN R -e "install.packages(c('tidyr', 'dplyr', 'magrittr', 'httr', 'jsonlite', 'plumber'), repos = 'http://cran.us.r-project.org')"

# Create /app dir and it set as working directory
RUN mkdir /app
WORKDIR /app

# Copy relevant files and directories
COPY . /app

# Expose port and run web server
EXPOSE 8000
ENTRYPOINT ["R", "-e", "r = plumber::plumb('endpoints.R'); r$run(port = 8000, host = '0.0.0.0')"]