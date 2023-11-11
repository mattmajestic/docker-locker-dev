# Use an official TensorFlow image as a base
FROM tensorflow/tensorflow:latest

# Upgrade TensorBoard
RUN pip install --upgrade tensorboard

# Set the working directory inside the container
WORKDIR /app

# Set the entry point for the container
CMD ["tensorboard", "--db", "sqlite:/root/.tensorboard.db", "--logdir", "/logs", "--bind_all"]

# Expose the TensorBoard port
EXPOSE 6006
