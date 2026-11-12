#use python based image
FROM python:3.10-slim

#set working directory
WORKDIR / app

#copy project files
COPY ./app

#installs dependencies
RUN  pip install --no-cache-dir -r requirements.txt

#expose the flak port
EXPOSE 5000

#run the program in app
CMD ["python", "app.y"]