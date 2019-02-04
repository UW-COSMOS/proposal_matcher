FROM ubuntu:xenial
RUN apt-get update
RUN apt-get install -y curl \
	ca-certificates \
	bzip2 \
	libx11-6
RUN adduser --disabled-password --gecos '' --shell /bin/bash user
ENV HOME=/home/user
RUN chmod 777 /home/user
WORKDIR /home/user
RUN curl -so miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
	&& chmod +x miniconda.sh
USER user
RUN ~/miniconda.sh -b -p ~/miniconda \
 && rm ~/miniconda.sh
ENV PATH=/home/user/miniconda/bin:$PATH
ENV CONDA_AUTO_UPDATE_CONDA=false
RUN /home/user/miniconda/bin/conda install conda-build \
 && /home/user/miniconda/bin/conda create -y --name py36 python=3.6.5 \
 && /home/user/miniconda/bin/conda clean -ya
ENV CONDA_DEFAULT_ENV=py36
ENV CONDA_PREFIX=/home/user/miniconda/envs/$CONDA_DEFAULT_ENV
ENV PATH=$CONDA_PREFIX/bin:$PATH
RUN conda install -y pandas numpy
RUN conda clean -ya

