FROM debian:bullseye

SHELL ["/bin/bash", "-c"]

ARG ASDF_VERSION=v0.11.1
ARG DIRENV_VERSION=2.32.2
ARG PYTHON_VERSION=3.11.4
ARG NODE_VERSION=18.13.0
ENV PIPENV_VENV_IN_PROJECT=true

RUN apt-get update -y && apt-get install -y \
  curl gcc make git zip unzip jq openssl ca-certificates gnupg lsb-release groff default-mysql-client pkg-config zlib1g-dev libffi-dev libbz2-dev libncurses5-dev libreadline-dev libssl-dev libsqlite3-dev liblzma-dev

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg \
  && echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null \
  && apt-get update -y && apt-get -y install docker-ce docker-ce-cli containerd.io docker-compose-plugin

RUN mkdir -p /go/src/$SRC_MODULE && chmod -R 777 /go
RUN chsh -s /bin/bash

WORKDIR /work/py-sandbox

RUN git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch ${ASDF_VERSION} \
  && echo '. ~/.asdf/asdf.sh' >> ~/.bash_profile \
  && echo '. ~/.asdf/completions/asdf.bash' >> ~/.bash_profile \
  && echo 'asdf direnv setup --shell bash --version ${DIRENV_VERSION}' >> ~/.bash_profile \
  && . ~/.asdf/asdf.sh \
  && . ~/.asdf/completions/asdf.bash \
  && asdf plugin-add direnv https://github.com/asdf-community/asdf-direnv.git \
  && asdf direnv setup --shell bash --version ${DIRENV_VERSION} \
  && asdf global direnv ${DIRENV_VERSION} \
  && asdf plugin-add awscli https://github.com/MetricMike/asdf-awscli.git \
  && asdf install awscli latest:2 \
  && asdf global awscli latest \
  && asdf plugin-add python \
  && asdf install python ${PYTHON_VERSION} \
  && asdf global python ${PYTHON_VERSION} \
  && pip install pipenv \
  && pipenv install --dev \
  && asdf plugin add nodejs https://github.com/asdf-vm/asdf-nodejs.git \
  && asdf install nodejs ${NODE_VERSION}
