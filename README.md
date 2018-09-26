# Virtual Device Host

## Description

This solution allows to decouple communicating "Internet of Things"-based devices.
This decoupling allows to simplify device communication and usage as well as to influence the exchanged data. 
Exchanged data can then be aggregated, projected or simply modified to be published to a MQTT broker as data of a so-called *virtual device*. Effectively, this allows to virtualize IoT devices and thus abstract from existing sensors and actors.
Focus of the solution lies in extensibility as well as configurability to allow the solution to potentially act as a platform for future projects.

## Setup

1. install dependencies

```
sudo apt-get install libxml2-dev
sudo apt-get install libxslt-dev
```

2. create virtual environment (for example: *python3 -m venv vdh-venv*)

```
python3 -m venv vdh-venv
```

3. load virtual environment

```
source vdh-venv/bin/activate
```

4. install pip dependencies

```
pip install -r requirements.txt
```

## Manual usage

1. if necessary, create configuration strategy file in directory *Configuration* (look inside for examples)

2. load virtual environment

```
source vdh-venv/bin/activate
```

3. run with configuration strategy file name as argument

```
python VDHApp.py MyFirstConfigurationStrategy
```

## Background usage

1. if necessary, create configuration strategy file in directory *Configuration* (look inside for examples)

2. follow guide in [wiki](/wiki/Set-up-as-background-service-(daemon))

## License

[LGPL-3.0 License](/LICENSE)
