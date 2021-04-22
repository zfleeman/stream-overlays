# stream-overlays
Dockerized Flask application that I use for my broadcasts in OBS.

### Docker Run
The `docker run` command can be run with a volume mount to keep a log of questions that have already been asked. This prevents duplicate questions.

```
docker run -v /local/docker/questions:/usr/app/questions -p 3030:3030 zachfleeman/stream-overlays
```