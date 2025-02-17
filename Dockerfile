# Using Python Slim-Buster
FROM koala21/kampangbot:buster
#
# Clone repo and prepare working directory
#
RUN git clone -b toxic-kampang https://github.com/Musthofaalfian/Toxic /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Musthofaalfian/Toxic/toxic-kampang/requirements.txt

EXPOSE 80 433

# Finalization
CMD ["python3","-m","userbot"]
