# GPT Neo Serving

## Build Docker Image

You can choose to use the one of the following method:

* `Dockerfile`
  * `docker buildx build -t <docker_hub_user_name>/<image_name> --push .`
* `build.envd`
  * `envd build -f :gpt_serving --output type=image,name=docker.io/<docker_hub_user_name>/<image_name> --push`
