
# FedUp

FedUp is a web application for aggregating news from RSS/Atom feeds. The goal of the project is to provide a clear stream of current articles, with support for searching, filtering by time range, and sorting by different signals such as recency, popularity, or user preferences.

The application does not publish full third-party articles. It works with headlines, short descriptions, and links to the original sources.

## What the application can do

- loads news from selected RSS/Atom sources,
- stores new articles and continuously removes outdated data,
- supports user login and registration,
- supports registration verification by e-mail,
- allows users to like articles,
- lets users hide selected news channels,
- provides full-text search,
- groups similar articles into thematic clusters,
- displays articles in a web interface,
- links users to the original publisher's website.

## How it works

The project is split into a backend and a frontend.

The backend regularly loads data from news feeds, parses RSS/Atom XML, compares newly found articles with already stored data, and saves only relevant new items. It uses a separate search engine for searching and a cache for faster access to selected data.

The application also creates embeddings from article text and uses text similarity to group articles that refer to the same topic. This makes it possible to show not only a regular news stream, but also a view of broader thematic connections.

The frontend is a simple web interface where users can log in, read articles, filter the stream, manage channels, and browse thematic groups.

## Technologies

```text
Python                  The main language powering the backend, frontend, and database communication.
FastAPI                 Used for middleware, rate limiting, and the API itself. => Separate FE and BE.
Flask                   Used to connect templates, forms, and the overall interaction with the API.
PostgreSQL              Used for storing all persistent data, vectors, and occasional vector operations.
Valkey (Redis)          Used for caching. (For example registration state or expiring tokens)
ElasticSearch           Used for keyword-based search across articles.
Docker + Compose        Used to simplify deployment and organize the individual parts of the project.
GitHub Actions          Used for the CI/CD pipeline.
SentenceTransformers    Used to create and compare vectors. (384-dimensional embeddings - paraphrase-multilingual-MiniLM-L12-v2)
HTML + CSS + JS         The basic stack for building the web interface.
Bulma                   Used for explicit styling classes. (I used Bootstrap too often, so I wanted the application to look a bit different)
Jinja2                  Used for creating templates and displaying data from the backend.
...                     The project contains many other technologies, but they are not considered part of its core.
```

## Deployment

The project is deployed at https://fedup.live

The registration process is restricted due to copyright reasons -> THE PROJECT IS NOT INTENDED FOR THE GENERAL PUBLIC

The project runs on a rented VPS. The main parts of the project are containerized with Docker, and the CI/CD pipeline is implemented through GitHub Actions.

## Project thoughts

I am learning programming, and this topic felt close to me because I want to stay informed about what is happening in the world.

That is why I decided to build the project in a way that would teach me as much as possible and connect Python, semantic features, vector-based data, and the deployment process itself.

And the main goal was, of course, to build something I know I will actually use, while also bringing some value compared to classic ways of consuming media content.
