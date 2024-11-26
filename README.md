# TuneCast 🎵🌦️

TuneCast is a FastAPI-based project that provides song recommendations tailored to the current weather in a specified location.

---

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Example](#api-example)

---

## Description

TuneCast fetches real-time weather data for a given location and uses this information to provide song recommendations that match the mood of the weather. Whether it's sunny, rainy, or cloudy, TuneCast suggests the perfect music to complement the atmosphere.

---

## Features

- Fetch weather data for any requested location.
- Get personalized song recommendations based on the weather (e.g., sunny days may suggest upbeat songs, while rainy days may recommend calm music).
- Simple and fast API built with FastAPI.
- Easy to integrate with any weather data provider.

---

## Installation

### Prerequisites

Make sure you have the following installed:

- Docker (for containerized environment)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/tunecast.git
    cd tunecast
    ```

2. Build the Docker image:
    ```bash
    docker build -t tunecast .
    ```

---

## Usage

Once the Docker image is built, you can run the application using Docker:

```bash
docker run -p 80:80 tunecast
```

---

## API Example

To test the API, use the following URL structure:
```bash
    http://0.0.0.0/api/v1/weather?location=barcelona
```

This will make a request to the /api/v1/weather endpoint with the location query parameter set to barcelona. The response will contain weather data for the given location and the song recommendations that match the mood of the weather.


