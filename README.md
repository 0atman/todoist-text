Deploy this with docker, then hit `http://hostname/[todoist api key]` to get a plain-text form of your todoist tasks

## CMD

```shell
$ docker run -p5000:5000 0atman/todoist-text
```
# Requirements

100MB disk, 30MB ram

Here's what my RAM usage looks like after hitting the endpoint a few times:

![2017-06-23-151735_635x221_scrot](https://user-images.githubusercontent.com/114097/27486197-b9e2c918-5827-11e7-835c-43f1a1473269.png)
