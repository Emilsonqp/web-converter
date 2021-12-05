FROM ubuntu:18.04
LABEL maintainer="Your Name <youremailaddress@provider.com>"
RUN apt-get update && apt-get install -y \
        software-properties-common
    RUN add-apt-repository ppa:deadsnakes/ppa
    RUN apt-get update && apt-get install -y \
        python3.7 \
        python3-pip
    RUN python3.7 -m pip install pip
    RUN apt-get update && apt-get install -y \
        python3-distutils \
        python3-setuptools
    RUN python3.7 -m pip install pip --upgrade pip
ADD . /converter
# COPY ./converter/requirements.txt /converter/requirements.txt
WORKDIR /converter/converter
RUN pip install -r requirements.txt
WORKDIR /converter/converter/app
EXPOSE 5000
CMD ["python3", "app.py"]



# FROM ubuntu:18.04
# # Set the working directory to /user-segmentation
# RUN mkdir -p ./sup-user-segmentation
# WORKDIR ./sup-user-segmentation
# #Copy requirment.txt
# COPY requirements.txt ./
# # Install any needed packages specified in requirements.txt
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# # Copy the current directory contents into the container at /user-segmentation
# COPY . ./
# # Make port 8080 available to the world outside this container
# EXPOSE 8080
# # Run migrations and server.py when the container launches
# ENTRYPOINT ["/bin/sh", "-c" , "flask db upgrade && sfx-py-trace server.py"]