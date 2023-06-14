# still developing, might have error
# Use the official PostgreSQL image as the base image
FROM postgres

# Set environment
ENV POSTGRES_PASSWORD=yao123
ENV POSTGRES_DB=tfprimate

# Mount file
COPY ./raw_data ./data 

# Expose the port
EXPOSE 5432

# Run container
CMD ["postgres"]