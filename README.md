
[![Build and push Docker image](https://github.com/openthisworld/legendary-computing-machine/actions/workflows/docker_hub.yml/badge.svg)](https://github.com/openthisworld/legendary-computing-machine/actions/workflows/docker_hub.yml)

legendary-computing-machine
OpenAI DALL-E-2 in docker container

#ENG VERSION


Instructions for using the container with image_generator.py

Required software

To work with the container, you need to install Docker. Installation instructions can be found on the Docker website.

Building the container

Download the Dockerfile and image_generator.py file to the same directory.
Open a terminal and navigate to this directory.
Build the container with the following command:

docker build -t <container_name> .

Running the container

To run the container, use the following command:

docker run -e PROMPT="<prompt_text>" -e API_KEY="<api_key>" -v <path_to_directory_on_host_machine>:/app <container_name>

Where:

<prompt_text> is the text that will be used to generate the image.
<api_key> is the API key required to call the API.
<path_to_directory_on_host_machine> is the path to the directory on the host machine where the generated image will be saved.
<container_name> is the name you gave the container during the build process.
Example usage
For example, if you want to generate an image with the text "Hello, World!" and save it to the /home/user/images directory, the command to run the container would be:

docker run -e PROMPT="Hello, World!" -e API_KEY="your_api_key" -v /home/user/images:/app image_generator

After running the container, a file named image.jpg containing the generated image will be saved in the /home/user/images directory.


#RUS VERSION


Инструкция по использованию контейнера с image_generator.py
Необходимое ПО

Для работы с контейнером необходимо установить Docker. Инструкции по установке можно найти на сайте Docker.

Сборка контейнера

Скачайте файл Dockerfile и файл image_generator.py в одну директорию.
Откройте терминал и перейдите в эту директорию.
Соберите контейнер с помощью команды:

docker build -t <имя_контейнера> .

Запуск контейнера

Для запуска контейнера используйте команду:

docker run -e PROMPT="<текст_приглашения>" -e API_KEY="<ключ_API>" -v <путь_к_директории_на_хост_машине>:/app <имя_контейнера>


При этом:

<путь_к_директории_на_хост_машине> - это путь к директории на хост-машине, куда будет сохранено сгенерированное изображение.
<имя_контейнера> - это имя, которое вы задали во время сборки контейнера.

Пример использования
Предположим, что вы хотите сгенерировать изображение с текстом "Hello, World!" и сохранить его в директорию /home/user/images. 

В этом случае команда для запуска контейнера будет выглядеть так:

docker run -e PROMPT="Hello, World!" -e API_KEY="your_api_key" -v /home/user/images:/app image_generator

После запуска контейнера в директории /home/user/images будет сохранен файл с именем image.jpg, содержащий сгенерированное изображение.

Genered with ChatGPT :)
